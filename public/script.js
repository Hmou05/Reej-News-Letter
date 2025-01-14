let status = document.querySelector("#status");

if (window.ononline) {
    status.textContent = "online";
    status.style.color = "rgb(0, 222, 96)";
} else {
    status.textContent = "offline";
    status.style.color = "red";
}