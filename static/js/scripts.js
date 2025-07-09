document.addEventListener("DOMContentLoaded", function () {
    console.log("✨ scripts.js loaded correctamente!");

    // Confirmación antes de enviar formularios (opcional)
    const forms = document.querySelectorAll("form");
    forms.forEach(form => {
        form.addEventListener("submit", function (e) {
            if (form.dataset.confirm === "true") {
                const confirmSubmit = confirm("¿Seguro que querés continuar?");
                if (!confirmSubmit) {
                    e.preventDefault();
                }
            }
        });
    });

    // Validación para formulario de búsqueda vacío
    const searchForm = document.querySelector('form.search-form');
    if (searchForm) {
        searchForm.addEventListener("submit", function (e) {
            const input = searchForm.querySelector("input[type='text']");
            if (input && input.value.trim() === "") {
                e.preventDefault();
                alert("Por favor escribí algo para buscar (・_・;)");
            }
        });
    }

    // Scroll suave para enlaces internos
    const links = document.querySelectorAll('a[href^="#"]');
    links.forEach(link => {
        link.addEventListener("click", function (e) {
            const target = document.querySelector(this.getAttribute("href"));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: "smooth" });
            }
        });
    });

    // Highlight temporal de resultados (si los tenés)
    const highlights = document.querySelectorAll(".highlight");
    highlights.forEach(el => {
        el.style.transition = "background 1s ease";
        el.style.backgroundColor = "#333";
        setTimeout(() => {
            el.style.backgroundColor = "transparent";
        }, 2000);
    });
});
