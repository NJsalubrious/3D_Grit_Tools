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

  // --- Video demo lightbox (clips stream from Cloudflare R2) ---
  // VIDEO_BASE: the R2 bucket's PUBLIC URL (must end with "/").
  // This is the public dev URL (R2 > 3d-grit-assets > Settings > Public Development URL),
  // NOT the S3 API endpoint (*.r2.cloudflarestorage.com), which needs auth.
  // To use a custom domain later, just change this one string.
  var VIDEO_BASE = "https://pub-e32d0586a45344c98cee1a56fa11418b.r2.dev/";
  var lightbox = document.getElementById("video-lightbox");
  if (lightbox) {
    var lbVideo = document.getElementById("lightbox-video");
    var lbClose = document.getElementById("video-lightbox-close");
    var lbTitle = document.getElementById("video-lightbox-title");

    var openVideo = function (file, label, tool) {
      if (!file) return;
      lbVideo.src = VIDEO_BASE + encodeURIComponent(file);
      if (lbTitle) lbTitle.textContent = label || "";
      lightbox.classList.add("active");
      lightbox.setAttribute("aria-hidden", "false");
      document.body.style.overflow = "hidden";
      var p = lbVideo.play();
      if (p && p.catch) p.catch(function () {});
      if (window.GRIT && window.GRIT.track) {
        window.GRIT.track("demo_play", { tool: tool || null, video: file });
      }
    };

    var closeVideo = function () {
      lightbox.classList.remove("active");
      lightbox.setAttribute("aria-hidden", "true");
      document.body.style.overflow = "";
      lbVideo.pause();
      lbVideo.removeAttribute("src");
      lbVideo.load();
    };

    document.querySelectorAll("[data-video]").forEach(function (el) {
      el.addEventListener("click", function (e) {
        e.preventDefault();
        openVideo(el.getAttribute("data-video"),
                  el.getAttribute("data-video-title"),
                  el.getAttribute("data-tool"));
      });
    });

    if (lbClose) lbClose.addEventListener("click", closeVideo);
    lightbox.addEventListener("click", function (e) { if (e.target === lightbox) closeVideo(); });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && lightbox.classList.contains("active")) closeVideo();
    });
  }

  // --- Inline demo players (the two main demos play in place, with native
  //     fullscreen). Swap a data-inline-video value to a YouTube/Vimeo URL
  //     later and it auto-embeds instead of streaming the R2 .mp4. ---
  document.querySelectorAll("[data-inline-video]").forEach(function (el) {
    el.addEventListener("click", function () {
      if (el.getAttribute("data-playing")) return;   // already swapped to a player
      var src = el.getAttribute("data-inline-video");
      if (!src) return;
      el.setAttribute("data-playing", "1");
      el.classList.add("is-playing");

      var node;
      var yt = src.match(/(?:youtube\.com\/(?:watch\?v=|embed\/)|youtu\.be\/)([\w-]{11})/);
      var vm = src.match(/vimeo\.com\/(?:video\/)?(\d+)/);
      if (yt || vm) {
        node = document.createElement("iframe");
        node.src = yt ? "https://www.youtube.com/embed/" + yt[1] + "?autoplay=1"
                      : "https://player.vimeo.com/video/" + vm[1] + "?autoplay=1";
        node.setAttribute("allow", "autoplay; fullscreen; picture-in-picture");
        node.setAttribute("allowfullscreen", "");
        node.setAttribute("title", "Demo video");
      } else {
        node = document.createElement("video");
        node.src = VIDEO_BASE + encodeURIComponent(src);
        node.controls = true;          // native controls include fullscreen
        node.autoplay = true;
        node.setAttribute("playsinline", "");
      }
      el.innerHTML = "";
      el.appendChild(node);
      if (node.play) { var p = node.play(); if (p && p.catch) p.catch(function () {}); }
      if (window.GRIT && window.GRIT.track) {
        window.GRIT.track("demo_play", { tool: el.getAttribute("data-tool") || null, video: src, mode: "inline" });
      }
    });
  });

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
