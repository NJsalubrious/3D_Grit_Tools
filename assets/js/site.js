/* ============================================================
   3D GRIT — shared page behaviors
   Nav background, mobile menu, scroll-reveal, soft-gate modal,
   and contact form submit. Loaded on every page.
   ============================================================ */
(function () {
  "use strict";

  // --- Scroll-based nav background ---
  var nav = document.getElementById("main-nav");
  if (nav) {
    window.addEventListener("scroll", function () {
      nav.classList.toggle("scrolled", window.scrollY > 20);
    });
  }

  // --- Mobile menu ---
  var mobileToggle = document.getElementById("mobile-toggle");
  var mobileMenu = document.getElementById("mobile-menu");
  if (mobileToggle && mobileMenu) {
    mobileToggle.addEventListener("click", function () { mobileMenu.classList.toggle("open"); });
    mobileMenu.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () { mobileMenu.classList.remove("open"); });
    });
  }

  // --- Scroll-reveal ---
  if ("IntersectionObserver" in window) {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) { entry.target.classList.add("visible"); observer.unobserve(entry.target); }
      });
    }, { threshold: 0.15 });
    document.querySelectorAll(".animate-in").forEach(function (el) { observer.observe(el); });
  } else {
    document.querySelectorAll(".animate-in").forEach(function (el) { el.classList.add("visible"); });
  }

  // --- Soft-gate modal (opens on any download_free CTA) ---
  var modal = document.getElementById("capture-modal");
  if (modal) {
    var modalClose = document.getElementById("modal-close-btn");
    var captureForm = document.getElementById("capture-form");
    var successState = document.getElementById("modal-success-state");
    var modalHeader = modal.querySelector(".modal-header");
    var pendingTool = null;

    document.querySelectorAll('[data-track="download_free"]').forEach(function (btn) {
      btn.addEventListener("click", function (e) {
        e.preventDefault();
        pendingTool = btn.getAttribute("data-tool") || null;
        modal.classList.add("active");
        modal.setAttribute("aria-hidden", "false");
      });
    });

    var closeModal = function () {
      modal.classList.remove("active");
      modal.setAttribute("aria-hidden", "true");
      setTimeout(function () {
        if (captureForm) captureForm.style.display = "block";
        if (modalHeader) modalHeader.style.display = "block";
        if (successState) successState.style.display = "none";
        if (captureForm) captureForm.reset();
      }, 300);
    };

    if (modalClose) modalClose.addEventListener("click", closeModal);
    modal.addEventListener("click", function (e) { if (e.target === modal) closeModal(); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && modal.classList.contains("active")) closeModal(); });

    if (captureForm) {
      captureForm.addEventListener("submit", function (e) {
        e.preventDefault();
        var email = document.getElementById("capture-email").value;
        if (window.GRIT && window.GRIT.track) {
          window.GRIT.track("email_capture", { tool: pendingTool, email: email });
        }
        if (captureForm) captureForm.style.display = "none";
        if (modalHeader) modalHeader.style.display = "none";
        if (successState) successState.style.display = "block";
        setTimeout(closeModal, 3000);
      });
    }
  }

  // --- Contact form ---
  var contactForm = document.getElementById("contact-form");
  if (contactForm) {
    var status = document.getElementById("contact-status");
    contactForm.addEventListener("submit", function (e) {
      e.preventDefault();
      var data = {
        name: document.getElementById("contact-name").value,
        email: document.getElementById("contact-email").value,
        subject: document.getElementById("contact-subject").value,
        message: document.getElementById("contact-message").value
      };
      if (window.GRIT && window.GRIT.track) window.GRIT.track("contact_submit", data);
      if (status) { status.textContent = "Message sent. We'll be in touch."; status.className = "form-status ok"; }
      contactForm.reset();
    });
  }
})();
