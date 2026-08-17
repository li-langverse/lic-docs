/* Notebook sketches — science, engineering, and computing plates. */
(function () {
  var THEMES = [
    {
      test: /language|compiler|verification|semantics|testing|security/,
      pack: ["ast", "logic", "turing", "transistor", "oscilloscope"],
    },
    {
      test: /physics|numerics|research/,
      pack: ["pendulum", "gyroscope", "oscilloscope", "energy-reactor", "chem-reactor"],
    },
    {
      test: /architecture|guide|getting-started|ecosystem|contributing/,
      pack: ["truss", "cogs", "engine", "robot", "transistor"],
    },
    {
      test: /game-dev|demo/,
      pack: ["rocket", "airplane", "satellite", "robot", "gyroscope"],
    },
  ];

  var FALLBACK = ["pendulum", "truss", "ast", "cogs", "logic", "engine"];

  function assetBase() {
    var logo = document.querySelector(".md-header__button.md-logo img, .md-logo img");
    if (logo && logo.src) {
      return logo.src.replace(/li-mark\.svg(?:\?.*)?$/, "sketches/");
    }
    var icon = document.querySelector('link[rel="shortcut icon"], link[rel="icon"]');
    if (icon && icon.href) {
      return icon.href.replace(/li-mark\.svg(?:\?.*)?$/, "sketches/");
    }
    return "assets/sketches/";
  }

  function hash(s) {
    var h = 0;
    for (var i = 0; i < s.length; i++) {
      h = (Math.imul(31, h) + s.charCodeAt(i)) | 0;
    }
    return Math.abs(h);
  }

  function packFor(path) {
    for (var i = 0; i < THEMES.length; i++) {
      if (THEMES[i].test.test(path)) return THEMES[i].pack;
    }
    return FALLBACK;
  }

  function plate(base, name) {
    return (
      '<figure class="li-plate"><img src="' +
      base +
      name +
      '.png" alt=""></figure>'
    );
  }

  function mount() {
    document.querySelectorAll(".li-margin-folio, .li-lab--page").forEach(function (n) {
      n.remove();
    });

    if (document.querySelector(".li-lab:not(.li-lab--page)")) return;

    var path = location.pathname.replace(/\/+$/, "") || "/";
    var pack = packFor(path);
    if (!pack.length) return;

    var h = hash(path);
    var picks = [];
    var i;
    for (i = 0; i < Math.min(4, pack.length); i++) {
      picks.push(pack[(h + i * 2) % pack.length]);
    }

    var base = assetBase();
    var article = document.querySelector(".md-content__inner");
    var content = document.querySelector(".md-content");
    if (!article || !content) return;

    var lab = document.createElement("div");
    lab.className = "li-lab li-lab--page";
    lab.setAttribute("aria-hidden", "true");
    lab.innerHTML =
      '<p class="li-lab__cap">Notebook</p>' +
      picks.map(function (name) {
        return plate(base, name);
      }).join("");
    article.appendChild(lab);

    var folio = document.createElement("div");
    folio.className = "li-margin-folio";
    folio.setAttribute("aria-hidden", "true");
    folio.innerHTML =
      '<figure class="li-plate li-plate--tr"><img src="' +
      base +
      picks[0] +
      '.png" alt=""></figure>' +
      '<figure class="li-plate li-plate--bl"><img src="' +
      base +
      picks[picks.length - 1] +
      '.png" alt=""></figure>';
    content.prepend(folio);
  }

  if (window.document$) {
    document$.subscribe(mount);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", mount);
  } else {
    mount();
  }
})();
