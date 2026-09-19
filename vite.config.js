import { defineConfig } from "vite";
import { resolve } from "path";

const root = resolve(__dirname);

export default defineConfig({
  root,
  base: "./",
  build: {
    outDir: "dist",
    emptyOutDir: true,
    rollupOptions: {
      input: {
        home: resolve(root, "index.html"),

        arIndex: resolve(root, "ar/index.html"),
        arServices: resolve(root, "ar/services.html"),
        arPortfolio: resolve(root, "ar/portfolio.html"),
        arAbout: resolve(root, "ar/about.html"),
        arContact: resolve(root, "ar/contact.html"),

        enIndex: resolve(root, "en/index.html"),
        enServices: resolve(root, "en/services.html"),
        enPortfolio: resolve(root, "en/portfolio.html"),
        enAbout: resolve(root, "en/about.html"),
        enContact: resolve(root, "en/contact.html"),

        svcWeb: resolve(root, "services/web-development.html"),
        svcLaravel: resolve(root, "services/laravel.html"),
        svcWordpress: resolve(root, "services/wordpress.html"),
        svcMobile: resolve(root, "services/mobile-apps.html"),
        svcEcommerce: resolve(root, "services/ecommerce.html"),
        svcUiUx: resolve(root, "services/ui-ux.html"),

        prjNaseem: resolve(root, "projects/naseem.html"),
        prjRecipe: resolve(root, "projects/recipe-app.html"),
        prjAboKartona: resolve(root, "projects/abo-kartona.html"),

        privacy: resolve(root, "privacy.html"),
        terms: resolve(root, "terms.html"),
      },
    },
  },
  server: {
    port: 5173,
    open: "/ar/index.html",
  },
});
