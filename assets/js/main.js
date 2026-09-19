/* =========================================================
   NOVIX — main.js
   Mobile drawer, sticky header, scroll reveal, FAQ accordion,
   contact form validation + toasts, back-to-top
   ========================================================= */
(function () {
  "use strict";

  /* ---------- Sticky header ---------- */
  const header = document.querySelector(".site-header");
  const onScroll = () => {
    if (!header) return;
    header.classList.toggle("is-scrolled", window.scrollY > 12);
    const backToTop = document.querySelector(".back-to-top");
    if (backToTop) backToTop.classList.toggle("show", window.scrollY > 500);
  };
  document.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* ---------- Mobile drawer ---------- */
  const menuToggle = document.querySelector(".menu-toggle");
  const drawer = document.querySelector(".mobile-drawer");
  const backdrop = document.querySelector(".drawer-backdrop");
  const drawerClose = document.querySelector(".drawer-close");

  function openDrawer() {
    drawer && drawer.classList.add("open");
    backdrop && backdrop.classList.add("open");
    document.body.style.overflow = "hidden";
  }
  function closeDrawer() {
    drawer && drawer.classList.remove("open");
    backdrop && backdrop.classList.remove("open");
    document.body.style.overflow = "";
  }
  menuToggle && menuToggle.addEventListener("click", openDrawer);
  drawerClose && drawerClose.addEventListener("click", closeDrawer);
  backdrop && backdrop.addEventListener("click", closeDrawer);
  document
    .querySelectorAll(".mobile-drawer a")
    .forEach((a) => a.addEventListener("click", closeDrawer));

  /* ---------- Back to top ---------- */
  const backToTop = document.querySelector(".back-to-top");
  backToTop &&
    backToTop.addEventListener("click", () =>
      window.scrollTo({ top: 0, behavior: "smooth" }),
    );

  /* ---------- Scroll reveal (single orchestrated pass) ---------- */
  const revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && revealEls.length) {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("in-view");
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -40px 0px" },
    );
    revealEls.forEach((el) => io.observe(el));
  } else {
    revealEls.forEach((el) => el.classList.add("in-view"));
  }

  /* ---------- FAQ accordion ---------- */
  document.querySelectorAll(".faq-item").forEach((item) => {
    const q = item.querySelector(".faq-q");
    const a = item.querySelector(".faq-a");
    if (!q || !a) return;
    q.addEventListener("click", () => {
      const isOpen = item.classList.contains("open");
      item.parentElement
        .querySelectorAll(".faq-item.open")
        .forEach((openItem) => {
          if (openItem !== item) {
            openItem.classList.remove("open");
            openItem.querySelector(".faq-a").style.maxHeight = null;
          }
        });
      item.classList.toggle("open", !isOpen);
      a.style.maxHeight = !isOpen ? a.scrollHeight + "px" : null;
    });
  });

  /* ---------- Toast notifications ---------- */
  function ensureToastStack() {
    let stack = document.querySelector(".toast-stack");
    if (!stack) {
      stack = document.createElement("div");
      stack.className = "toast-stack";
      document.body.appendChild(stack);
    }
    return stack;
  }

  window.showToast = function (message, type) {
    const stack = ensureToastStack();
    const toast = document.createElement("div");
    toast.className = "toast toast-" + (type || "success");
    toast.innerHTML =
      '<span class="toast-dot"></span><span>' + message + "</span>";
    stack.appendChild(toast);
    requestAnimationFrame(() => toast.classList.add("show"));
    setTimeout(() => {
      toast.classList.remove("show");
      setTimeout(() => toast.remove(), 400);
    }, 3800);
  };
/* ---------- Contact form validation + API submission ---------- */

const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

function setFieldError(field, message) {
  const wrap = field.closest(".field");
  if (!wrap) return;

  let err = wrap.querySelector(".field-error");

  if (!err) {
    err = document.createElement("div");
    err.className = "field-error";
    wrap.appendChild(err);
  }

  if (message) {
    wrap.classList.add("has-error");
    err.textContent = message;
  } else {
    wrap.classList.remove("has-error");
    err.textContent = "";
  }
}

function validateField(field) {
  // Honeypot is intentionally ignored by client-side validation.
  // Laravel validates it on the server.
  if (field.classList.contains("hp-field")) {
    return true;
  }

  const value = field.value.trim();

  let msgs = {};

  try {
    msgs = field.dataset.msgs
      ? JSON.parse(field.dataset.msgs)
      : {};
  } catch (error) {
    console.warn("Invalid data-msgs JSON:", error);
  }

  if (field.hasAttribute("required") && !value) {
    setFieldError(
      field,
      msgs.required || "This field is required"
    );

    return false;
  }

  if (
    field.type === "email" &&
    value &&
    !EMAIL_RE.test(value)
  ) {
    setFieldError(
      field,
      msgs.email || "Enter a valid email address"
    );

    return false;
  }

  setFieldError(field, "");

  return true;
}

document.querySelectorAll("form.contact-form").forEach((form) => {
  const fields = form.querySelectorAll(
    "input, textarea, select"
  );

  fields.forEach((field) => {
    if (
      field.type !== "hidden" &&
      !field.classList.contains("hp-field")
    ) {
      field.addEventListener("blur", () => {
        validateField(field);
      });

      field.addEventListener("input", () => {
        if (field.closest(".field")?.classList.contains("has-error")) {
          validateField(field);
        }
      });
    }
  });

  form.addEventListener("submit", async function (e) {
    e.preventDefault();

    let valid = true;

    fields.forEach((field) => {
      if (!validateField(field)) {
        valid = false;
      }
    });

    if (!valid) {
      window.showToast(
        form.dataset.errorMsg ||
          "Please check the highlighted fields",
        "error"
      );

      return;
    }

    const submitBtn = form.querySelector('[type="submit"]');

    const originalText = submitBtn
      ? submitBtn.textContent
      : "";

    if (submitBtn) {
      submitBtn.disabled = true;

      submitBtn.textContent =
        form.dataset.sendingMsg || "Sending...";
    }

    /*
     * Build payload from the form.
     *
     * Expected Laravel fields:
     * name
     * email
     * phone
     * service
     * budget
     * message
     * website (honeypot)
     */
    const formData = new FormData(form);

    const payload = Object.fromEntries(
      formData.entries()
    );

    Object.keys(payload).forEach((key) => {
      if (typeof payload[key] === "string") {
        payload[key] = payload[key].trim();
      }
    });

    /*
     * Laravel API endpoint.
     *
     * Can be overridden from HTML using:
     *
     * data-api-endpoint="https://your-domain.com/api/v1/contact"
     */
    const endpoint =
      form.dataset.apiEndpoint ||
      "http://127.0.0.1:8000/api/v1/contact";

    try {
      const response = await fetch(endpoint, {
        method: "POST",

        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
        },

        body: JSON.stringify(payload),
      });

      let data = {};

      try {
        data = await response.json();
      } catch (jsonError) {
        throw new Error(
          `Server returned an invalid response (${response.status})`
        );
      }

      /*
       * Laravel validation failed.
       */
      if (response.status === 422) {
        if (data.errors) {
          Object.entries(data.errors).forEach(
            ([fieldName, messages]) => {
              const field = form.querySelector(
                `[name="${fieldName}"]`
              );

              if (field && Array.isArray(messages)) {
                setFieldError(field, messages[0]);
              }
            }
          );
        }

        throw new Error(
          data.message ||
            "Please check the highlighted fields."
        );
      }

      /*
       * Other server errors.
       */
      if (!response.ok) {
        throw new Error(
          data.message ||
            `Request failed with status ${response.status}`
        );
      }

      /*
       * Success.
       */
      window.showToast(
        form.dataset.successMsg ||
          "Your message has been sent successfully.",
        "success"
      );

      form.reset();

      /*
       * Remove previous validation errors after reset.
       */
      fields.forEach((field) => {
        setFieldError(field, "");
      });

    } catch (error) {
      console.error("NOVIX contact form error:", error);

      window.showToast(
        error.message ||
          form.dataset.errorMsg ||
          "An error occurred. Please try again.",
        "error"
      );

    } finally {
      if (submitBtn) {
        submitBtn.disabled = false;
        submitBtn.textContent = originalText;
      }
    }
  });
});

  /* ---------- Portfolio filter (if present) ---------- */
  const filterBtns = document.querySelectorAll(
    ".portfolio-filter [data-filter]",
  );
  const portfolioItems = document.querySelectorAll("[data-category]");
  filterBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      filterBtns.forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      const filter = btn.dataset.filter;
      portfolioItems.forEach((item) => {
        const show = filter === "all" || item.dataset.category === filter;
        item.style.display = show ? "" : "none";
      });
    });
  });
})();
