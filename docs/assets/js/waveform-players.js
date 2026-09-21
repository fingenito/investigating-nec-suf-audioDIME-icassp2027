document.addEventListener("DOMContentLoaded", function () {
  if (typeof WaveSurfer === "undefined") return;

  document.querySelectorAll("[data-wsplayer]").forEach(function (el) {
    var btn = el.querySelector(".wsplayer-btn");
    var waveEl = el.querySelector(".wsplayer-wave");

    var ws = WaveSurfer.create({
      container: waveEl,
      url: el.getAttribute("data-src"),
      height: 32,
      waveColor: "#9fb8c8",
      progressColor: "#2C6E8C",
      cursorColor: "#B23A2E",
      barWidth: 2,
      barGap: 1,
      barRadius: 1,
      normalize: false,
    });

    btn.addEventListener("click", function () {
      ws.playPause();
    });
    ws.on("play", function () {
      btn.textContent = "⏸";
    });
    ws.on("pause", function () {
      btn.textContent = "▶";
    });
    ws.on("finish", function () {
      btn.textContent = "▶";
    });
  });
});
