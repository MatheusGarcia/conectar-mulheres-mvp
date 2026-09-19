const SAFE_EXIT_URL = "https://www.google.com/search?q=previs%C3%A3o+do+tempo";

document.querySelectorAll("[data-quick-exit]").forEach((button) => {
  button.addEventListener("click", () => window.location.replace(SAFE_EXIT_URL));
});

const whatsappForm = document.querySelector("[data-whatsapp-form]");
if (whatsappForm) {
  whatsappForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const phoneInput = document.querySelector("#contact-phone");
    const messageInput = document.querySelector("#contact-message");
    let phone = phoneInput.value.replace(/\D/g, "");
    if (phone.length === 10 || phone.length === 11) phone = `55${phone}`;
    if (phone.length < 12) {
      phoneInput.setCustomValidity("Informe o DDD e o número do WhatsApp.");
      phoneInput.reportValidity();
      return;
    }
    phoneInput.setCustomValidity("");
    const url = `https://wa.me/${phone}?text=${encodeURIComponent(messageInput.value.trim())}`;
    window.open(url, "_blank", "noopener,noreferrer");
  });
}
