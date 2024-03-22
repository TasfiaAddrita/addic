(() => {
  let youtubeRightControls;

  window.addEventListener("load", () => {
    const spotifyBtn = document.createElement("img");

    spotifyBtn.src = chrome.runtime.getURL("assets/spotifyLogoGreyMargin.png");
    spotifyBtn.className = "ytp-button " + "spotify-btn";

    youtubeRightControls =
      document.getElementsByClassName("ytp-right-controls")[0];

    youtubeRightControls.insertAdjacentElement("afterbegin", spotifyBtn);
  });
})();
