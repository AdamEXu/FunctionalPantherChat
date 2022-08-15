window.addEventListener("beforeunload", function () {
    var bodyelement = document.querySelector("content");
    bodyelement.classList.add("animate-out");
    // bodyelement.classList.add("animate-in")
});