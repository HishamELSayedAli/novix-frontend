# NOVIX — Frontend

A complete, production-ready **frontend-only** multi-page website for a digital
agency brand ("NOVIX"), built with plain HTML/CSS/JavaScript and bundled with
Vite. Cinematic dark-tech visual system: obsidian background, neon-orange glow
accents, glass surfaces, full Arabic (RTL) + English (LTR) support.

## Getting started

```bash
npm install
npm run dev       # local dev server, opens ar/index.html
npm run build      # production build into /dist
npm run preview    # preview the production build
```

No backend is required to browse the site. The contact form validates on the
client and is wired to POST JSON to `/api/contact` — swap that endpoint for
your real Laravel API route (see the commented `fetch()` block in
`assets/js/main.js`).

## Structure

```
/
├── ar/                     Arabic (RTL) pages: index, services, portfolio, about, contact
├── en/                     English (LTR) mirror of the same 5 pages
├── services/               6 dedicated service detail pages
├── projects/               4 case-study pages (Naseem, Recipe App, Abo Kartona, Hodhod)
├── assets/
│   ├── css/style.css       Design system (tokens, components, layout)
│   ├── js/main.js          Mobile menu, sticky header, reveal-on-scroll,
│   │                       FAQ accordion, form validation + toasts
│   └── img/                Placeholder imagery (swap with real photography/renders)
├── privacy.html
├── terms.html
├── index.html              Redirects to /ar/index.html (default site language)
├── vite.config.js          Multi-page build entry map
├── package.json
└── generate.py             The generator used to produce every HTML page from
                             shared header/footer + content data (edit this,
                             then re-run `python3 generate.py`, to update copy
                             across the whole site consistently)
```

## Notes

- **Language toggle**: AR/EN switch in the header links between the matching
  page in each language folder. The six `/services/*.html` and four
  `/projects/*.html` deep pages are Arabic-first (matching the reference
  design); their EN toggle falls back to the English services/portfolio
  listing.
- **Editing content**: rather than hand-editing 20+ HTML files, edit the data
  dictionaries at the top of `generate.py` (services, projects, testimonials,
  FAQ, copy strings) and re-run the generator — every page rebuilds
  consistently from one source of truth.
- **Images**: `assets/img/*.jpg` are placeholder gradient renders so the
  layout is fully visible out of the box. Replace them with real photography,
  product shots, or 3D renders before shipping.
- **Accessibility**: visible focus states, reduced-motion support, semantic
  landmarks (`header`, `main`, `section`, `footer`) are included throughout.
