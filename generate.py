# -*- coding: utf-8 -*-
"""
NOVIX static site generator.
Produces every HTML page defined in the required folder structure by
composing a shared header/footer shell with page-specific content blocks.
Run: python3 generate.py
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

# ------------------------------------------------------------------ #
# Shared data
# ------------------------------------------------------------------ #

SITE = {
    "name": "NOVIX",
    "tagline_ar": "Design · Develop · Create",
    "tagline_en": "Design · Develop · Create",
    "phone": "+20 10 1234 5678",
    "email": "contact.novix.info@gmail.com",
    "address_ar": "القاهرة - مصر",
    "address_en": "Cairo, Egypt",
    "domain": "https://www.novix.com",
}

SERVICES = [
    {
        "slug": "web-development",
        "icon": "code",
        "title_ar": "تطوير المواقع الإلكترونية",
        "title_en": "Web Development",
        "desc_ar": "مواقع أعمال ومتاجر إلكترونية سريعة وآمنة مبنية على Laravel وPHP.",
        "desc_en": "Fast, secure business sites and web apps built on Laravel and PHP.",
        "bullets_ar": ["مواقع الأعمال والشركات", "تطوير باستخدام Laravel", "أداء عالي وأمان متقدم"],
        "bullets_en": ["Corporate & business sites", "Laravel-powered builds", "High performance & security"],
    },
    {
        "slug": "laravel",
        "icon": "layers",
        "title_ar": "تطوير Laravel",
        "title_en": "Laravel Development",
        "desc_ar": "أنظمة ولوحات تحكم مخصصة مبنية على إطار عمل Laravel لأداء موثوق وقابل للتوسع.",
        "desc_en": "Custom systems and dashboards built on Laravel for reliable, scalable backends.",
        "bullets_ar": ["أنظمة إدارة محتوى مخصصة", "واجهات برمجية (APIs) آمنة", "قواعد بيانات منظمة وقابلة للتوسع"],
        "bullets_en": ["Custom CMS & admin panels", "Secure REST APIs", "Scalable database architecture"],
    },
    {
        "slug": "wordpress",
        "icon": "globe",
        "title_ar": "تطوير مواقع WordPress",
        "title_en": "WordPress Development",
        "desc_ar": "مواقع ووردبريس مرنة وسهلة الإدارة مصممة خصيصًا لاحتياجات عملك.",
        "desc_en": "Flexible, easy-to-manage WordPress sites tailored to your business needs.",
        "bullets_ar": ["قوالب مخصصة بالكامل", "متاجر ووكومرس", "تحسين سرعة وأداء الموقع"],
        "bullets_en": ["Fully custom themes", "WooCommerce stores", "Speed & performance tuning"],
    },
    {
        "slug": "mobile-apps",
        "icon": "smartphone",
        "title_ar": "تطوير تطبيقات الموبايل",
        "title_en": "Mobile App Development",
        "desc_ar": "تطبيقات Flutter وAndroid سريعة وسلسة على مختلف المنصات.",
        "desc_en": "Smooth, high-performance Flutter and Android apps across platforms.",
        "bullets_ar": ["تطبيقات Flutter متعددة المنصات", "تطبيقات Android أصلية", "تجربة استخدام سلسة"],
        "bullets_en": ["Cross-platform Flutter apps", "Native Android builds", "Smooth, intuitive UX"],
    },
    {
        "slug": "ecommerce",
        "icon": "cart",
        "title_ar": "المتاجر الإلكترونية",
        "title_en": "E-commerce",
        "desc_ar": "متاجر إلكترونية متكاملة بأنظمة دفع وشحن مرنة لتنمية مبيعاتك.",
        "desc_en": "Full-featured online stores with flexible payment & shipping integrations.",
        "bullets_ar": ["بوابات دفع متعددة", "إدارة مخزون وطلبات", "تصميم يحفّز على الشراء"],
        "bullets_en": ["Multiple payment gateways", "Inventory & order management", "Conversion-focused design"],
    },
    {
        "slug": "ui-ux",
        "icon": "figma",
        "title_ar": "تصميم واجهات المستخدم UI/UX",
        "title_en": "UI/UX Design",
        "desc_ar": "تصميم احترافي يجمع بين الجمال وسهولة الاستخدام لكل شاشة.",
        "desc_en": "Professional design that balances aesthetics with genuine usability.",
        "bullets_ar": ["أبحاث تجربة المستخدم", "نماذج تفاعلية (Prototypes)", "أنظمة تصميم متكاملة"],
        "bullets_en": ["User research & flows", "Interactive prototypes", "Complete design systems"],
    },
]

PROJECTS = [
    {
        "slug": "naseem",
        "title": "Naseem Blog",
        "title_ar": "مدونة نسيم",
        "stack": ["Laravel", "PHP", "MySQL"],
        "cat": "web",
        "live_demo": "https://naseem-production.up.railway.app/",
        "github": "https://github.com/HishamELSayedAli/Naseem",
        "summary_ar": "منصة مدونات عربية بتصميم RTL كامل، تدعم النشر والتصنيفات والتعليقات.",
        "summary_en": "An Arabic-first RTL blogging platform with publishing, categories, and comments.",
        "challenge_ar": "بناء منصة تدوين عربية بالكامل تدعم اتجاه RTL بشكل صحيح في كل عنصر تصميمي، مع لوحة تحكم منفصلة لإدارة المحتوى.",
        "challenge_en": "Deliver a fully Arabic RTL blogging experience — correct mirroring across every UI element — alongside a separate content-management control panel.",
        "solution_ar": "تم تطوير أكثر من 18 صفحة واجهة أمامية ولوحة تحكم من 6 صفحات، بنظام تصميم مخصص بألوان نيلي وسماوي وكهرماني، تمهيدًا لدمجها لاحقًا كقوالب Blade في Laravel.",
        "solution_en": "Built 18+ front-end pages plus a 6-page admin panel with a custom indigo/cyan/amber design system, structured as a frontend prototype for later integration as Laravel Blade templates.",
        "features_ar": ["نشر وتحرير المقالات", "تصنيفات ووسوم", "لوحة تحكم إدارية", "تصميم زجاجي (Glassmorphism)"],
        "features_en": ["Article publishing & editing", "Categories & tags", "Admin control panel", "Glassmorphism visual system"],
    },
    {
        "slug": "recipe-app",
        "title": "Recipe App",
        "title_ar": "تطبيق الوصفات",
        "stack": ["PHP", "MySQL", "JavaScript"],
        "cat": "web",
        "live_demo": "https://recipeapp345.wuaze.com/index.php",
        "github": "https://github.com/HishamELSayedAli/RecipeApp",
        "summary_ar": "تطبيق وصفات يتيح تصفح وإضافة الوصفات وحفظها كمفضلة.",
        "summary_en": "A recipe application for browsing, adding, and favoriting recipes.",
        "challenge_ar": "إدارة قاعدة بيانات وصفات متنامية مع صور وتفاصيل دقيقة، وضمان استقرار الاستعلامات وسرعة عرض الصور.",
        "challenge_en": "Manage a growing recipe database with images and detailed metadata, while keeping queries stable and image rendering fast.",
        "solution_ar": "بُني التطبيق بلغة PHP الأصلية مع MySQL، ويشمل صفحات تصفح وبحث وتفاصيل، مع تحسينات مستمرة على بنية قاعدة البيانات وأداء الصفحات.",
        "solution_en": "Built with native PHP and MySQL, covering browsing, search, and detail views — with ongoing refinement of the database schema and page performance.",
        "features_ar": ["تصفح وبحث الوصفات", "إضافة وصفات جديدة", "قائمة مفضلة", "صفحات تفاصيل غنية"],
        "features_en": ["Recipe browsing & search", "Add new recipes", "Favorites list", "Rich detail pages"],
    },
    {
        "slug": "abo-kartona",
        "title": "Abo Kartona",
        "title_ar": "أبو كرتونة",
        "stack": ["Flutter", "Riverpod", "Realm"],
        "cat": "mobile",
        "live_demo": "https://abo-kartona.wuaze.com/",
        "github": "https://github.com/HishamELSayedAli/Abo_Kartona_APP",
        "summary_ar": "تطبيق موبايل تجاري بأداء عالٍ وقاعدة بيانات محلية سريعة.",
        "summary_en": "A commerce mobile app with strong performance and a fast local database.",
        "challenge_ar": "تحقيق تجربة استخدام سريعة وسلسة حتى في ظل اتصال إنترنت غير مستقر.",
        "challenge_en": "Deliver a fast, smooth experience even under unreliable network conditions.",
        "solution_ar": "تم استخدام Flutter مع إدارة حالة Riverpod وقاعدة بيانات Realm المحلية لتوفير أداء فوري وتخزين موثوق دون اتصال.",
        "solution_en": "Built with Flutter, Riverpod state management, and a local Realm database for instant responsiveness and reliable offline storage.",
        "features_ar": ["تصفح المنتجات", "دعم العمل بدون إنترنت", "إدارة حالة تفاعلية", "أداء سريع"],
        "features_en": ["Product browsing", "Offline-first support", "Reactive state management", "Fast performance"],
    },
    
]

TESTIMONIALS = [
    {"name": "Ahmed Tarek", "role_ar": "صاحب متجر إلكتروني", "role_en": "Online Store Owner",
     "text_ar": "فريق راقٍ ومحترف. نفذوا لي المتجر الإلكتروني بدقة وأظهروا التزامًا حقيقيًا بمواعيد التسليم.",
     "text_en": "A refined, professional team. They delivered my online store with precision and real commitment to deadlines."},
    {"name": "Sara Mohamed", "role_ar": "مطوّرة محتوى", "role_en": "Content Developer",
     "text_ar": "تصميم الموقع كان يتماشى مع هويتنا البصرية بسهولة ويسر، وتعاملهم مع جميع الأجهزة كان ممتازًا.",
     "text_en": "The design matched our visual identity effortlessly, and cross-device handling was excellent."},
    {"name": "Omar El-Sayed", "role_ar": "مؤسس شركة ناشئة", "role_en": "Startup Founder",
     "text_ar": "احترافية في التعامل وجودة في التنفيذ. مستمرون في اقتراحوكم لأصدقائي ومعظم عملائي عن ثقة.",
     "text_en": "Professional throughout, with quality execution. I keep recommending them to friends and clients with full confidence."},
]

PROCESS = [
    {"n": "01", "title_ar": "تواصل معنا", "title_en": "Get in Touch",
     "desc_ar": "أخبرنا عن فكرتك واحتياجاتك خلال جلسة تعارف أولية.",
     "desc_en": "Tell us about your idea and needs in a first discovery call."},
    {"n": "02", "title_ar": "تحليل وتخطيط", "title_en": "Analyze & Plan",
     "desc_ar": "نقوم بدراسة المشروع ووضع خارطة طريق واضحة للتنفيذ.",
     "desc_en": "We study the project and lay out a clear execution roadmap."},
    {"n": "03", "title_ar": "التصميم والتطوير", "title_en": "Design & Develop",
     "desc_ar": "نقوم بدراسة المشروع وتصميمه وتطويره بجودة عالية.",
     "desc_en": "We design and build the product with meticulous attention to quality."},
    {"n": "04", "title_ar": "التسليم والدعم", "title_en": "Deliver & Support",
     "desc_ar": "نسلّم المشروع في الوقت المحدد ونوفر دعمًا مستمرًا بعد التسليم.",
     "desc_en": "We ship on schedule and provide continuous post-launch support."},
]

FAQ = [
    {"q_ar": "كم تستغرق مدة تنفيذ المشروع؟", "q_en": "How long does a project take?",
     "a_ar": "تختلف المدة حسب حجم المشروع ومتطلباته، ونقدم جدولًا زمنيًا واضحًا بعد جلسة التحليل الأولى.",
     "a_en": "Timelines vary by project scope. We share a clear schedule right after the discovery session."},
    {"q_ar": "هل تقدمون الدعم بعد تسليم المشروع؟", "q_en": "Do you offer support after delivery?",
     "a_ar": "نعم، نوفر باقات دعم مستمر لصيانة وتحديث مشروعك بعد الإطلاق.", "a_en": "Yes, we offer ongoing support plans to maintain and update your product after launch."},
    {"q_ar": "ما هي التقنيات التي تعملون بها؟", "q_en": "Which technologies do you work with?",
     "a_ar": "نعمل بشكل أساسي مع Laravel وPHP وFlutter وWordPress إلى جانب تصميم UI/UX متكامل.",
     "a_en": "We primarily work with Laravel, PHP, Flutter, and WordPress, alongside full UI/UX design."},
    {"q_ar": "هل يمكنني رؤية أعمال سابقة قبل البدء؟", "q_en": "Can I see previous work before starting?",
     "a_ar": "بالطبع، يمكنك تصفح قسم أعمالنا للاطلاع على مشاريع فعلية أنجزناها.",
     "a_en": "Of course — browse our portfolio section to see real projects we've delivered."},
]

# ------------------------------------------------------------------ #
# Icon set (inline SVG, currentColor)
# ------------------------------------------------------------------ #
ICONS = {
    "code": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M8 4 2 12l6 8M16 4l6 8-6 8" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "layers": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="m12 2 9 5-9 5-9-5 9-5Z"/><path d="m3 12 9 5 9-5M3 17l9 5 9-5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "globe": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.5 3.8 5.7 3.8 9s-1.3 6.5-3.8 9c-2.5-2.5-3.8-5.7-3.8-9S9.5 5.5 12 3Z"/></svg>',
    "smartphone": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="6" y="2" width="12" height="20" rx="2"/><path d="M11 18h2" stroke-linecap="round"/></svg>',
    "cart": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="9" cy="20" r="1.4"/><circle cx="18" cy="20" r="1.4"/><path d="M2 3h2l2.6 12.6a2 2 0 0 0 2 1.6H18a2 2 0 0 0 2-1.6L21.5 8H6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "figma": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M9 2h4a3 3 0 0 1 0 6H9V2Z"/><path d="M9 8h4a3 3 0 0 1 0 6H9V8Z"/><path d="M9 14h3a3 3 0 1 1-3 3v-3Z"/><circle cx="15.5" cy="17" r="2.5"/></svg>',
    "check": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M20 6 9 17l-5-5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "arrow": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M5 12h14M13 6l6 6-6 6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "quality": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="m12 2 2.6 5.6 6.1.6-4.6 4.1 1.3 6-5.4-3.1L6.6 18.3l1.3-6-4.6-4.1 6.1-.6L12 2Z" stroke-linejoin="round"/></svg>',
    "clock": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 2" stroke-linecap="round"/></svg>',
    "support": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 13a8 8 0 0 1 16 0" stroke-linecap="round"/><path d="M4 13v4a2 2 0 0 0 2 2h1v-6H4Z"/><path d="M20 13v4a2 2 0 0 1-2 2h-1v-6h3Z"/></svg>',
    "price": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 2v20M17 5.5c0-1.9-2.2-3.5-5-3.5s-5 1.6-5 3.5S9.2 9 12 9s5 1.6 5 3.5-2.2 3.5-5 3.5-5-1.6-5-3.5" stroke-linecap="round"/></svg>',
    "phone": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .3 2 .6 3a2 2 0 0 1-.5 2L8 10a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2-.5c1 .3 2 .5 3 .6a2 2 0 0 1 1.7 2Z" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "mail": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m2 6 10 7 10-7" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "pin": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 21s7-6.6 7-11.5A7 7 0 0 0 5 9.5C5 14.4 12 21 12 21Z"/><circle cx="12" cy="9.5" r="2.4"/></svg>',
    "up": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M12 19V5M5 12l7-7 7 7" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "menu": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 7h16M4 12h16M4 17h16" stroke-linecap="round"/></svg>',
    "close": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m6 6 12 12M18 6 6 18" stroke-linecap="round"/></svg>',
    "fb": '<svg width="17" height="17" viewBox="0 0 24 24" fill="currentColor"><path d="M13.5 21v-8.1h2.7l.4-3.2h-3.1V7.7c0-.9.3-1.6 1.6-1.6h1.7V3.2C15.9 3.1 14.8 3 13.6 3c-2.6 0-4.4 1.6-4.4 4.5v2.2H6.5v3.2h2.7V21h4.3Z"/></svg>',
    "x": '<svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M3 3l7.4 9.6L3 21h2.4l6.2-6.9 5 6.9H21l-7.7-10L20.6 3h-2.4l-5.7 6.3L7.4 3H3Z"/></svg>',
    "ig": '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.3" cy="6.7" r="1"/></svg>',
    "li": '<svg width="17" height="17" viewBox="0 0 24 24" fill="currentColor"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5ZM3 9h4v12H3V9Zm7 0h3.8v1.7h.1c.5-1 1.9-2 3.8-2 4 0 4.8 2.7 4.8 6.1V21h-4v-5.6c0-1.3 0-3-1.8-3s-2.1 1.4-2.1 2.9V21h-4V9Z"/></svg>',
    "yt": '<svg width="17" height="17" viewBox="0 0 24 24" fill="currentColor"><path d="M22 12s0-3.2-.4-4.7a3 3 0 0 0-2.1-2.1C17.9 4.8 12 4.8 12 4.8s-5.9 0-7.5.4A3 3 0 0 0 2.4 7.3C2 8.8 2 12 2 12s0 3.2.4 4.7a3 3 0 0 0 2.1 2.1c1.6.4 7.5.4 7.5.4s5.9 0 7.5-.4a3 3 0 0 0 2.1-2.1C22 15.2 22 12 22 12Zm-12 3V9l5 3-5 3Z"/></svg>',
    "github": '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 0 0-3.2 19.5c.5.1.7-.2.7-.5v-1.7c-2.8.6-3.4-1.3-3.4-1.3-.4-1.2-1-1.5-1-1.5-.9-.6.1-.6.1-.6 1 .1 1.5 1 1.5 1 .9 1.5 2.3 1.1 2.9.8.1-.7.4-1.1.6-1.4-2.2-.3-4.6-1.1-4.6-5a4 4 0 0 1 1-2.7c-.1-.3-.5-1.3.1-2.6 0 0 .9-.3 2.9 1a10 10 0 0 1 5.2 0c2-1.3 2.9-1 2.9-1 .6 1.3.2 2.3.1 2.6a4 4 0 0 1 1 2.7c0 3.9-2.4 4.7-4.6 5 .4.3.7 1 .7 2v2.9c0 .3.2.6.7.5A10 10 0 0 0 12 2Z"/></svg>',
    "external": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7 17 17 7M8 7h9v9" stroke-linecap="round" stroke-linejoin="round"/></svg>',
}

TRUST_POINTS = [
    {"icon": "price", "ar": "أسعار مناسبة", "en": "Fair pricing"},
    {"icon": "clock", "ar": "الالتزام بالمواعيد", "en": "On-time delivery"},
    {"icon": "support", "ar": "دعم مستمر", "en": "Continuous support"},
    {"icon": "quality", "ar": "جودة عالية", "en": "High quality"},
]

NAV_PAGES = [
    ("index", "الرئيسية", "Home"),
    ("services", "الخدمات", "Services"),
    ("portfolio", "أعمالنا", "Portfolio"),
    ("about", "من نحن", "About"),
    ("contact", "تواصل معنا", "Contact"),
]

T = {
    "ar": {
        "dir": "rtl", "lang": "ar",
        "start_project": "ابدأ مشروعك", "view_work": "شاهد أعمالنا",
        "read_more": "اعرف المزيد", "view_project": "عرض المشروع", "live_demo": "معاينة مباشرة",
        "our_services": "خدماتنا", "services_sub": "حلول شاملة لاحتياجاتك الرقمية",
        "services_lead": "نقدم مجموعة متكاملة من الخدمات التقنية والتصميمية لمساعدتك في تحقيق أهدافك.",
        "featured_work": "بعض من مشاريعنا المميزة", "work_sub": "أعمالنا",
        "work_lead": "نختار كل مشروع بعناية لنقدم أفضل النتائج بأعلى جودة.",
        "why_us": "لماذا نختار NOVIX؟", "why_sub": "أكثر مجرد مزوّد خدمات، بل شريك في نجاحك",
        "why_lead": "لا نقدم خدمات حرفية فقط، بل نعمل معك كشريك حقيقي لإنجاح مشروعك، ونحرص على تقديم أفضل الحلول التي تناسب احتياجاتك وميزانيتك.",
        "process_title": "كيف نعمل؟", "process_sub": "خطوات بسيطة نحو مشروعك",
        "process_lead": "نتبع منهجية واضحة لضمان تنفيذ مشروعك بجودة عالية ووفق احتياجاتك.",
        "testi_title": "آراء عملائنا", "testi_sub": "ماذا يقولون عنا؟", "testi_lead": "ثقة عملائنا هي أكبر شهادة على جودة خدماتنا.",
        "faq_title": "الأسئلة الشائعة", "faq_sub": "لديك سؤال؟", "faq_lead": "إجابات على أكثر الأسئلة شيوعًا حول خدماتنا وطريقة عملنا.",
        "cta_title": "مشروعك القادم يبدأ من هنا", "cta_sub": "تواصل معنا اليوم ودعنا نحوّل فكرتك إلى واقع رقمي احترافي.",
        "contact_title": "ابدأ مشروعك الآن", "contact_sub": "تواصل معنا",
        "contact_lead": "هل لديك فكرة؟ نحن هنا لمساعدتك في تحويلها إلى واقع رقمي.",
        "name": "الاسم", "email": "البريد الإلكتروني", "service_type": "نوع الخدمة", "budget": "الميزانية التقريبية",
        "details": "تفاصيل المشروع", "send": "إرسال الطلب", "select_service": "اختر الخدمة المناسبة",
        "select_budget": "اختر الميزانية المناسبة", "details_ph": "اكتب تفاصيل مشروعك هنا...",
        "name_ph": "أدخل اسمك", "email_ph": "example@domain.com",
        "about_title": "من نحن", "about_sub": "قصة NOVIX",
        "about_lead": "وكالة رقمية متخصصة في تصميم وتطوير المواقع والتطبيقات، نساعد الأفراد والشركات على بناء حضورهم الرقمي بجودة احترافية.",
        "mission": "رسالتنا", "mission_txt": "تمكين الشركات والأفراد من النمو رقميًا عبر حلول تقنية مدروسة وتصميم يحمل هوية مميزة.",
        "vision": "رؤيتنا", "vision_txt": "أن نكون الوجهة الأولى للشركات الطموحة الباحثة عن شريك تقني موثوق في المنطقة.",
        "values": "قيمنا", "values_txt": "الشفافية، الجودة، الالتزام بالمواعيد، والشغف بالتفاصيل الصغيرة.",
        "portfolio_title": "أعمالنا", "portfolio_sub": "مشاريع أنجزناها بفخر",
        "portfolio_lead": "تصفح مجموعة من المشاريع التي نفذناها لعملائنا في مجالات مختلفة.",
        "filter_all": "الكل", "filter_web": "مواقع ويب", "filter_mobile": "تطبيقات موبايل",
        "services_page_title": "خدماتنا", "services_page_lead": "نقدم مجموعة متكاملة من الخدمات الرقمية المصممة لمساعدتك على النمو.",
        "challenge": "التحدي", "solution": "الحل", "features": "أبرز المميزات", "tech_stack": "التقنيات المستخدمة",
        "related_projects": "مشاريع مشابهة", "back_to_portfolio": "الرجوع لكل الأعمال",
        "footer_desc": "وكالة رقمية متخصصة في تصميم وتطوير المواقع والتطبيقات وحلول الأعمال الرقمية.",
        "footer_links": "روابط سريعة", "footer_services": "خدماتنا", "footer_contact": "تواصل معنا",
        "rights": "جميع الحقوق محفوظة NOVIX ©", "privacy": "سياسة الخصوصية", "terms": "الشروط والأحكام",
        "process_heading": "التزامنا خطوة بخطوة",
        "service_detail_lead": "تعرف على كيفية مساعدتنا لك في هذا المجال، من الفكرة وحتى الإطلاق.",
        "about_service": "عن هذه الخدمة", "our_process": "آلية عملنا", "get_started": "ابدأ الآن",
        "not_found": "الصفحة غير موجودة", "back_home": "العودة للرئيسية",
    },
    "en": {
        "dir": "ltr", "lang": "en",
        "start_project": "Start Your Project", "view_work": "View Our Work",
        "read_more": "Learn More", "view_project": "View Project", "live_demo": "Live Demo",
        "our_services": "Our Services", "services_sub": "Complete solutions for your digital needs",
        "services_lead": "We offer a full range of technical and design services to help you reach your goals.",
        "featured_work": "Some of Our Featured Projects", "work_sub": "Our Work",
        "work_lead": "Every project is chosen with care so we can deliver the best results at the highest quality.",
        "why_us": "Why Choose NOVIX?", "why_sub": "More than a vendor — a partner in your success",
        "why_lead": "We don't just deliver services; we work alongside you to make your project succeed, offering the solutions that fit your needs and budget.",
        "process_title": "How We Work", "process_sub": "Simple steps toward your project",
        "process_lead": "We follow a clear methodology to make sure your project is delivered to a high standard, on your terms.",
        "testi_title": "Client Voices", "testi_sub": "What our clients say", "testi_lead": "Our clients' trust is the best evidence of our quality.",
        "faq_title": "FAQ", "faq_sub": "Got a question?", "faq_lead": "Answers to the questions we hear most about our services and process.",
        "cta_title": "Your Next Project Starts Here", "cta_sub": "Get in touch today and let's turn your idea into a professional digital product.",
        "contact_title": "Start Your Project Now", "contact_sub": "Contact Us",
        "contact_lead": "Have an idea? We're here to help you turn it into digital reality.",
        "name": "Name", "email": "Email Address", "service_type": "Service Type", "budget": "Approximate Budget",
        "details": "Project Details", "send": "Send Request", "select_service": "Select a service",
        "select_budget": "Select a budget range", "details_ph": "Tell us about your project...",
        "name_ph": "Enter your name", "email_ph": "example@domain.com",
        "about_title": "About Us", "about_sub": "The NOVIX Story",
        "about_lead": "A digital agency specialized in designing and building websites and apps, helping individuals and businesses grow their digital presence.",
        "mission": "Our Mission", "mission_txt": "Empowering businesses and individuals to grow digitally through thoughtful technology and distinctive design.",
        "vision": "Our Vision", "vision_txt": "To be the go-to technology partner for ambitious companies across the region.",
        "values": "Our Values", "values_txt": "Transparency, quality, punctuality, and a passion for the smallest details.",
        "portfolio_title": "Our Work", "portfolio_sub": "Projects we're proud of",
        "portfolio_lead": "Browse a selection of projects we've delivered for clients across different industries.",
        "filter_all": "All", "filter_web": "Websites", "filter_mobile": "Mobile Apps",
        "services_page_title": "Our Services", "services_page_lead": "A complete set of digital services designed to help you grow.",
        "challenge": "The Challenge", "solution": "The Solution", "features": "Key Features", "tech_stack": "Tech Stack",
        "related_projects": "Related Projects", "back_to_portfolio": "Back to all work",
        "footer_desc": "A digital agency specialized in websites, apps, and digital business solutions.",
        "footer_links": "Quick Links", "footer_services": "Services", "footer_contact": "Contact",
        "rights": "All Rights Reserved NOVIX ©", "privacy": "Privacy Policy", "terms": "Terms & Conditions",
        "process_heading": "Our step-by-step commitment",
        "service_detail_lead": "See how we help you in this area, from the first idea to launch.",
        "about_service": "About This Service", "our_process": "Our Process", "get_started": "Get Started",
        "not_found": "Page Not Found", "back_home": "Back to Home",
    },
}

print("Data module loaded OK")

# ------------------------------------------------------------------ #
# Header / Footer / shared chrome
# ------------------------------------------------------------------ #

def render_header(lang, base, active_key, lang_links):
    """
    lang: 'ar' | 'en' current page language
    base: relative prefix to project root ('../' or '')
    active_key: one of index/services/portfolio/about/contact/None
    lang_links: dict {'ar': href, 'en': href} for the language switch
    """
    t = T[lang]
    nav_items = ""
    for key, label_ar, label_en in NAV_PAGES:
        label = label_ar if lang == "ar" else label_en
        href = f"{base}{lang}/index.html" if key == "index" else f"{base}{lang}/{key}.html"
        active_cls = " active" if key == active_key else ""
        nav_items += f'<li><a href="{href}" class="{active_cls.strip()}">{label}</a></li>'

    ar_active = " active" if lang == "ar" else ""
    en_active = " active" if lang == "en" else ""

    return f"""
  <header class="site-header">
    <div class="container">
      <a href="{base}{lang}/index.html" class="brand">
        <span class="brand-mark">N</span>
        <span>{SITE['name']}</span>
      </a>
      <nav class="nav-main">
        <ul class="nav-links">{nav_items}</ul>
      </nav>
      <div class="header-actions">
        <div class="lang-toggle">
          <a href="{lang_links.get('ar', '#')}" class="{ar_active.strip()}">AR</a>
          <a href="{lang_links.get('en', '#')}" class="{en_active.strip()}">EN</a>
        </div>
        <a href="{base}{lang}/contact.html" class="btn btn-primary btn-sm">{t['start_project']} {ICONS['arrow']}</a>
        <button class="menu-toggle" aria-label="Menu">{ICONS['menu']}</button>
      </div>
    </div>
  </header>
  <div class="drawer-backdrop"></div>
  <aside class="mobile-drawer">
    <button class="drawer-close" aria-label="Close">{ICONS['close']}</button>
    <a href="{base}{lang}/index.html" class="brand"><span class="brand-mark">N</span><span>{SITE['name']}</span></a>
    <ul class="nav-links">{nav_items}</ul>
    <a href="{base}{lang}/contact.html" class="btn btn-primary btn-block">{t['start_project']}</a>
  </aside>
"""


def render_footer(lang, base):
    t = T[lang]
    service_links = ""
    for s in SERVICES:
        title = s["title_ar"] if lang == "ar" else s["title_en"]
        service_links += f'<li><a href="{base}services/{s["slug"]}.html">{title}</a></li>'

    quick_links = ""
    for key, label_ar, label_en in NAV_PAGES:
        label = label_ar if lang == "ar" else label_en
        href = f"{base}{lang}/index.html" if key == "index" else f"{base}{lang}/{key}.html"
        quick_links += f'<li><a href="{href}">{label}</a></li>'

    address = SITE["address_ar"] if lang == "ar" else SITE["address_en"]

    return f"""
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="{base}{lang}/index.html" class="brand"><span class="brand-mark">N</span><span>{SITE['name']}</span></a>
          <p>{t['footer_desc']}</p>
          <div class="social-row">
            <a href="#" aria-label="Facebook">{ICONS['fb']}</a>
            <a href="#" aria-label="X">{ICONS['x']}</a>
            <a href="#" aria-label="Instagram">{ICONS['ig']}</a>
            <a href="https://www.linkedin.com/company/ai-smart-technology" aria-label="LinkedIn">{ICONS['li']}</a>
            <a href="#" aria-label="YouTube">{ICONS['yt']}</a>
          </div>
        </div>
        <div class="footer-col">
          <h4>{t['footer_links']}</h4>
          <ul>{quick_links}</ul>
        </div>
        <div class="footer-col">
          <h4>{t['footer_services']}</h4>
          <ul>{service_links}</ul>
        </div>
        <div class="footer-col">
          <h4>{t['footer_contact']}</h4>
          <ul>
            <li class="flex items-center gap-1">{ICONS['phone']} {SITE['phone']}</li>
            <li class="flex items-center gap-1">{ICONS['mail']} {SITE['email']}</li>
            <li class="flex items-center gap-1">{ICONS['pin']} {address}</li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <span>{t['rights']} {2025}</span>
        <div class="legal-links">
          <a href="{base}privacy.html">{t['privacy']}</a>
          <a href="{base}terms.html">{t['terms']}</a>
        </div>
      </div>
    </div>
  </footer>
  <button class="back-to-top" aria-label="Back to top">{ICONS['up']}</button>
"""


def page_shell(lang, base, active_key, lang_links, title, description, body, canonical, extra_head="", json_ld=""):
    t = T[lang]
    og_locale = "ar_AR" if lang == "ar" else "en_US"
    return f"""<!DOCTYPE html>
<html lang="{t['lang']}" dir="{t['dir']}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:locale" content="{og_locale}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE['domain']}/assets/img/og-cover.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<link rel="icon" href="{base}assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{base}assets/css/style.css">
{extra_head}
{json_ld}
</head>
<body class="lang-{lang}">
{render_header(lang, base, active_key, lang_links)}
<main>
{body}
</main>
{render_footer(lang, base)}
<script src="{base}assets/js/main.js" defer></script>
</body>
</html>
"""


def reveal(html):
    return f'<div class="reveal">{html}</div>'


def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", path)


# ------------------------------------------------------------------ #
# Reusable content blocks
# ------------------------------------------------------------------ #

def block_hero(lang, base):
    t = T[lang]
    trust_html = ""
    for p in TRUST_POINTS:
        label = p["ar"] if lang == "ar" else p["en"]
        trust_html += f'<div class="trust-point">{ICONS["check"]}<span>{label}</span></div>'

    heading_ar = 'نحوّل أفكارك إلى <span class="accent">حلول رقمية</span> احترافية'
    heading_en = 'We turn your ideas into <span class="accent">professional</span> digital products'
    heading = heading_ar if lang == "ar" else heading_en

    lead_ar = "نصمم ونطور مواقع الويب وتطبيقات الموبايل والمتاجر الإلكترونية، لمساعدة الأفراد والشركات على بناء حضور رقمي قوي."
    lead_en = "We design and build websites, mobile apps, and online stores — helping individuals and businesses build a strong digital presence."
    lead = lead_ar if lang == "ar" else lead_en

    welcome_ar = f"مرحبًا بك في {SITE['name']}"
    welcome_en = f"Welcome to {SITE['name']}"

    return f"""
  <section class="hero">
    <div class="container">
      <div class="hero-copy">
        <span class="hero-badge"><span class="dot"></span>{welcome_ar if lang=='ar' else welcome_en}</span>
        <h1>{heading}</h1>
        <p class="lead">{lead}</p>
        <div class="hero-ctas">
          <a href="{base}{lang}/contact.html" class="btn btn-primary">{t['start_project']} {ICONS['arrow']}</a>
          <a href="{base}{lang}/portfolio.html" class="btn btn-outline">{t['view_work']}</a>
        </div>
        <div class="trust-points">{trust_html}</div>
      </div>
      <div class="hero-visual">
        <div class="hero-frame">
          <img src="{base}assets/img/hero-workspace.jpg" alt="{SITE['name']} workspace" width="640" height="480" loading="eager">
        </div>
        <div class="hero-float-card">{ICONS['quality']}<span>{'جودة احترافية' if lang=='ar' else 'Crafted quality'}</span></div>
      </div>
    </div>
  </section>
"""


def block_services_grid(lang, base, limit=6):
    t = T[lang]
    cards = ""
    for s in SERVICES[:limit]:
        title = s["title_ar"] if lang == "ar" else s["title_en"]
        desc = s["desc_ar"] if lang == "ar" else s["desc_en"]
        bullets = s["bullets_ar"] if lang == "ar" else s["bullets_en"]
        bullets_html = "".join(f"<li>{b}</li>" for b in bullets)
        cards += reveal(f"""
        <div class="glass-card service-card">
          <div class="service-icon">{ICONS[s['icon']]}</div>
          <h3>{title}</h3>
          <p class="text-muted" style="font-size:0.92rem">{desc}</p>
          <ul>{bullets_html}</ul>
          <a href="{base}services/{s['slug']}.html" class="card-link">{t['read_more']} {ICONS['arrow']}</a>
        </div>""")
    return f"""
  <section id="services">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">{t['our_services']}</span>
        <h2>{t['services_sub']}</h2>
        <p>{t['services_lead']}</p>
      </div>
      <div class="grid grid-3">{cards}</div>
    </div>
  </section>
"""


def block_portfolio_grid(lang, base, projects=None, with_filter=False):
    t = T[lang]
    projects = projects or PROJECTS
    filter_html = ""
    if with_filter:
        filter_html = f"""
      <div class="portfolio-filter flex justify-content-center gap-1 mb-3" style="justify-content:center;flex-wrap:wrap">
        <button class="btn btn-outline btn-sm active" data-filter="all">{t['filter_all']}</button>
        <button class="btn btn-outline btn-sm" data-filter="web">{t['filter_web']}</button>
        <button class="btn btn-outline btn-sm" data-filter="mobile">{t['filter_mobile']}</button>
      </div>"""
    cards = ""
    for p in projects:
        title = p["title_ar"] if lang == "ar" else p["title"]
        summary = p["summary_ar"] if lang == "ar" else p["summary_en"]
        tags = "".join(f'<span class="stack-tag">{s}</span>' for s in p["stack"])
        cards += reveal(f"""
        <div class="glass-card project-card" data-category="{p['cat']}">
          <div class="project-media"><img src="{base}assets/img/project-{p['slug']}.jpg" alt="{title}" loading="lazy" width="640" height="400"></div>
          <div class="project-body">
            <h3>{title}</h3>
            <p class="text-muted" style="font-size:0.9rem">{summary}</p>
            <div class="stack-tags">{tags}</div>
            <a href="{base}projects/{p['slug']}.html" class="card-link">{t['view_project']} {ICONS['arrow']}</a>
          </div>
        </div>""")
    return filter_html, f'<div class="grid grid-2">{cards}</div>'


def block_why_us(lang):
    t = T[lang]
    items = [
        ("quality", t.get("quality_h", "خدمة مخصصة" if lang == "ar" else "Tailored service"),
         "نصمم كل مشروع حسب احتياجاتك الفعلية دون قوالب جاهزة." if lang == "ar" else "Every project is shaped around your real needs, never a generic template."),
        ("support", "دعم مستمر" if lang == "ar" else "Ongoing support",
         "فريقنا معك بعد التسليم لضمان استقرار مشروعك." if lang == "ar" else "Our team stays with you after launch to keep things running smoothly."),
        ("price", "أسعار عادلة" if lang == "ar" else "Fair pricing",
         "نقدم أفضل قيمة مقابل الجودة التي نلتزم بها." if lang == "ar" else "We deliver strong value for the quality we commit to."),
        ("clock", "الالتزام بالمواعيد" if lang == "ar" else "On-time delivery",
         "نسلّم مشروعك في الوقت المحدد دون تأخير." if lang == "ar" else "We deliver your project on schedule, every time."),
    ]
    rows = "".join(reveal(f"""
      <div class="feature-row">
        <div class="icon-box">{ICONS[icon]}</div>
        <div><h4>{h}</h4><p>{d}</p></div>
      </div>""") for icon, h, d in items)
    return f"""
  <section class="tight">
    <div class="container grid grid-2" style="align-items:center">
      <div class="reveal">
        <span class="eyebrow">{t['why_sub']}</span>
        <h2 class="mt-1 mb-2">{t['why_us']}</h2>
        <p class="lead">{t['why_lead']}</p>
      </div>
      <div class="grid" style="gap:28px">{rows}</div>
    </div>
  </section>
"""


def block_process(lang):
    t = T[lang]
    steps = ""
    for i, p in enumerate(PROCESS):
        title = p["title_ar"] if lang == "ar" else p["title_en"]
        desc = p["desc_ar"] if lang == "ar" else p["desc_en"]
        active = " is-active" if i == 0 else ""
        steps += reveal(f"""
        <div class="glass-card process-step{active}">
          <span class="process-num">{p['n']}</span>
          <h3>{title}</h3>
          <p class="text-muted" style="font-size:0.9rem">{desc}</p>
        </div>""")
    return f"""
  <section>
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">{t['process_sub']}</span>
        <h2>{t['process_title']}</h2>
        <p>{t['process_lead']}</p>
      </div>
      <div class="grid grid-4">{steps}</div>
    </div>
  </section>
"""


def block_testimonials(lang, base):
    t = T[lang]
    cards = ""
    for i, tm in enumerate(TESTIMONIALS):
        role = tm["role_ar"] if lang == "ar" else tm["role_en"]
        text = tm["text_ar"] if lang == "ar" else tm["text_en"]
        cards += reveal(f"""
        <div class="glass-card testimonial-card">
          <div class="testimonial-stars">★★★★★</div>
          <p>{text}</p>
          <div class="testimonial-person">
            <img class="avatar" src="{base}assets/img/avatar-{i+1}.jpg" alt="{tm['name']}" loading="lazy" width="42" height="42">
            <div><strong>{tm['name']}</strong><span>{role}</span></div>
          </div>
        </div>""")
    return f"""
  <section class="tight">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">{t['testi_sub']}</span>
        <h2>{t['testi_title']}</h2>
        <p>{t['testi_lead']}</p>
      </div>
      <div class="grid grid-3">{cards}</div>
    </div>
  </section>
"""


def block_faq(lang):
    t = T[lang]
    items = ""
    for f in FAQ:
        q = f["q_ar"] if lang == "ar" else f["q_en"]
        a = f["a_ar"] if lang == "ar" else f["a_en"]
        items += f"""
        <div class="faq-item">
          <button class="faq-q">{q}<span class="plus">{ICONS['arrow']}</span></button>
          <div class="faq-a"><div class="faq-a-inner">{a}</div></div>
        </div>"""
    return f"""
  <section class="tight">
    <div class="container" style="max-width:820px">
      <div class="section-head reveal">
        <span class="eyebrow">{t['faq_sub']}</span>
        <h2>{t['faq_title']}</h2>
        <p>{t['faq_lead']}</p>
      </div>
      <div class="reveal">{items}</div>
    </div>
  </section>
"""


def block_cta(lang, base):
    t = T[lang]
    return f"""
  <section class="tight">
    <div class="container">
      <div class="cta-banner reveal">
        <div>
          <h2>{t['cta_title']}</h2>
          <p class="text-muted">{t['cta_sub']}</p>
        </div>
        <a href="{base}{lang}/contact.html" class="btn btn-primary">{t['start_project']} {ICONS['arrow']}</a>
      </div>
    </div>
  </section>
"""


def block_contact_form(lang): 
    t = T[lang]
    required_msg = "هذا الحقل مطلوب" if lang == "ar" else "This field is required"
    email_msg = "يرجى إدخال بريد إلكتروني صحيح" if lang == "ar" else "Please enter a valid email"
    import json as _json
    msgs = _json.dumps({"required": required_msg, "email": email_msg}, ensure_ascii=False)
    service_options = "".join(
        f'<option value="{s["slug"]}">{s["title_ar"] if lang=="ar" else s["title_en"]}</option>' for s in SERVICES
    )
    budgets = [" $500", "$500 - $1,500", "$1,500 - $5,000", "$5,000+"]
    budget_options = "".join(f'<option value="{b}">{b}</option>' for b in budgets)
    success_msg = "تم إرسال طلبك بنجاح، سنتواصل معك قريبًا" if lang == "ar" else "Your request was sent — we'll be in touch soon"
    error_msg = "يرجى مراجعة الحقول المظللة" if lang == "ar" else "Please check the highlighted fields"
    sending_msg = "جارٍ الإرسال..." if lang == "ar" else "Sending..."

    return f"""

      <form class="contact-form glass-card" data-success-msg="{success_msg}" data-error-msg="{error_msg}" data-sending-msg="{sending_msg}" data-api-endpoint="http://127.0.0.1:8000/api/v1/contact">
        <div class="field-row">
          <div class="field">
            <label for="name">{t['name']}</label>
            <input type="text" id="name" name="name" placeholder="{t['name_ph']}" data-msgs='{msgs}' required>
          </div>
          <div class="field">
            <label for="email">{t['email']}</label>
            <input type="email" id="email" name="email" placeholder="{t['email_ph']}" data-msgs='{msgs}' required>
          </div>
        </div>
        <div class="field-row">
          <div class="field">
            <label for="service">{t['service_type']}</label>
            <select id="service" name="service" data-msgs='{msgs}' required>
              <option value="">{t['select_service']}</option>
              {service_options}
            </select>
          </div>
          <div class="field">
            <label for="budget">{t['budget']}</label>
            <select id="budget" name="budget" data-msgs='{msgs}'>
              <option value="">{t['select_budget']}</option>
              {budget_options}
            </select>
          </div>
        </div>
        <div class="field">
          <label for="details">{t['details']}</label>
          <textarea id="details" name="message" rows="5" placeholder="{t['details_ph']}" data-msgs='{msgs}' required></textarea>
        </div>
        <button type="submit" class="btn btn-primary btn-block">{t['send']}</button>
      </form>
"""


# ------------------------------------------------------------------ #
# Page builders
# ------------------------------------------------------------------ #

def lang_links_for(page_key):
    """Return {'ar': href, 'en': href} for standard site pages (relative from lang folder)."""
    if page_key == "index":
        return {"ar": "../ar/index.html", "en": "../en/index.html"}
    return {"ar": f"../ar/{page_key}.html", "en": f"../en/{page_key}.html"}


def build_home(lang):
    base = "../"
    body = block_hero(lang, base)
    body += block_services_grid(lang, base)
    filter_html, grid_html = block_portfolio_grid(lang, base)
    t = T[lang]
    body += f"""
  <section class="tight">
    <div class="container">
      <div class="flex justify-between items-center mb-3 reveal" style="flex-wrap:wrap;gap:16px">
        <div>
          <span class="eyebrow">{t['work_sub']}</span>
          <h2 class="mt-1">{t['featured_work']}</h2>
        </div>
        <a href="{base}{lang}/portfolio.html" class="btn btn-outline btn-sm">{t['back_to_portfolio'] if False else (t['view_work'])}</a>
      </div>
      {grid_html}
    </div>
  </section>
"""
    body += block_why_us(lang)
    body += block_process(lang)
    body += block_testimonials(lang, base)
    body += f"""
  <section class="tight">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">{t['contact_sub']}</span>
        <h2>{t['contact_title']}</h2>
        <p>{t['contact_lead']}</p>
      </div>
      <div class="reveal" style="max-width:760px;margin-inline:auto">
        {block_contact_form(lang)}
      </div>
    </div>
  </section>
"""
    title = f"{SITE['name']} | {'حلول رقمية احترافية' if lang=='ar' else 'Professional Digital Solutions'}"
    desc = t['lead'] if 'lead' in t else t['services_lead']
    desc_ar = "نصمم ونطور مواقع الويب وتطبيقات الموبايل والمتاجر الإلكترونية لمساعدتك على النمو رقميًا."
    desc_en = "We design and build websites, mobile apps, and online stores to help you grow digitally."
    json_ld = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "{SITE['name']}",
  "url": "{SITE['domain']}",
  "email": "{SITE['email']}",
  "telephone": "{SITE['phone']}",
  "sameAs": []
}}
</script>"""
    html = page_shell(lang, base, "index", lang_links_for("index"), title,
                       desc_ar if lang == "ar" else desc_en, body,
                       f"{SITE['domain']}/{lang}/index.html", json_ld=json_ld)
    write(f"{lang}/index.html", html)


def build_services_page(lang):
    base = "../"
    t = T[lang]
    hero = f"""
  <section class="page-hero">
    <div class="container">
      <div class="breadcrumb"><a href="{base}{lang}/index.html">{t['our_services'] if False else NAV_PAGES[0][1] if lang=='ar' else NAV_PAGES[0][2]}</a><span>/</span><span>{t['services_page_title']}</span></div>
      <span class="eyebrow">{t['our_services']}</span>
      <h1 class="mt-1">{t['services_page_title']}</h1>
      <p class="lead" style="margin-inline:auto">{t['services_page_lead']}</p>
    </div>
  </section>
"""
    body = hero + block_services_grid(lang, base) + block_process(lang) + block_faq(lang) + block_cta(lang, base)
    html = page_shell(lang, base, "services", lang_links_for("services"),
                       f"{t['services_page_title']} | {SITE['name']}", t['services_page_lead'], body,
                       f"{SITE['domain']}/{lang}/services.html")
    write(f"{lang}/services.html", html)


def build_portfolio_page(lang):
    base = "../"
    t = T[lang]
    hero = f"""
  <section class="page-hero">
    <div class="container">
      <div class="breadcrumb"><a href="{base}{lang}/index.html">{NAV_PAGES[0][1] if lang=='ar' else NAV_PAGES[0][2]}</a><span>/</span><span>{t['portfolio_title']}</span></div>
      <span class="eyebrow">{t['portfolio_sub']}</span>
      <h1 class="mt-1">{t['portfolio_title']}</h1>
      <p class="lead" style="margin-inline:auto">{t['portfolio_lead']}</p>
    </div>
  </section>
"""
    filter_html, grid_html = block_portfolio_grid(lang, base, with_filter=True)
    body = hero + f'<section class="tight"><div class="container">{filter_html}{grid_html}</div></section>' + block_cta(lang, base)
    html = page_shell(lang, base, "portfolio", lang_links_for("portfolio"),
                       f"{t['portfolio_title']} | {SITE['name']}", t['portfolio_lead'], body,
                       f"{SITE['domain']}/{lang}/portfolio.html")
    write(f"{lang}/portfolio.html", html)


def build_about_page(lang):
    base = "../"
    t = T[lang]
    hero = f"""
  <section class="page-hero">
    <div class="container">
      <div class="breadcrumb"><a href="{base}{lang}/index.html">{NAV_PAGES[0][1] if lang=='ar' else NAV_PAGES[0][2]}</a><span>/</span><span>{t['about_title']}</span></div>
      <span class="eyebrow">{t['about_sub']}</span>
      <h1 class="mt-1">{t['about_title']}</h1>
      <p class="lead" style="margin-inline:auto">{t['about_lead']}</p>
    </div>
  </section>
"""
    cards = ""
    for icon, key_h, key_txt in [("quality", "mission", "mission_txt"), ("figma", "vision", "vision_txt"), ("check", "values", "values_txt")]:
        cards += reveal(f"""
        <div class="glass-card">
          <div class="service-icon">{ICONS[icon]}</div>
          <h3 class="mt-2">{t[key_h]}</h3>
          <p class="text-muted mt-1" style="font-size:0.92rem">{t[key_txt]}</p>
        </div>""")
    body = hero + f'<section class="tight"><div class="container grid grid-3">{cards}</div></section>'
    body += block_why_us(lang)
    body += block_testimonials(lang, base)
    body += block_cta(lang, base)
    html = page_shell(lang, base, "about", lang_links_for("about"),
                       f"{t['about_title']} | {SITE['name']}", t['about_lead'], body,
                       f"{SITE['domain']}/{lang}/about.html")
    write(f"{lang}/about.html", html)


def build_contact_page(lang):
    base = "../"
    t = T[lang]
    hero = f"""
  <section class="page-hero">
    <div class="container">
      <div class="breadcrumb"><a href="{base}{lang}/index.html">{NAV_PAGES[0][1] if lang=='ar' else NAV_PAGES[0][2]}</a><span>/</span><span>{t['contact_title']}</span></div>
      <span class="eyebrow">{t['contact_sub']}</span>
      <h1 class="mt-1">{t['contact_title']}</h1>
      <p class="lead" style="margin-inline:auto">{t['contact_lead']}</p>
    </div>
  </section>
"""
    address = SITE["address_ar"] if lang == "ar" else SITE["address_en"]
    info_col = f"""
      <div class="glass-card">
        <h3 class="mb-2">{t['contact_sub']}</h3>
        <div class="contact-info-item">{ICONS['phone']}<span>{SITE['phone']}</span></div>
        <div class="contact-info-item">{ICONS['mail']}<span>{SITE['email']}</span></div>
        <div class="contact-info-item">{ICONS['pin']}<span>{address}</span></div>
        <hr class="divider">
        <div class="social-row">
          <a href="#" aria-label="Facebook">{ICONS['fb']}</a>
          <a href="#" aria-label="X">{ICONS['x']}</a>
          <a href="#" aria-label="Instagram">{ICONS['ig']}</a>
          <a href="#" aria-label="LinkedIn">{ICONS['li']}</a>
        </div>
      </div>
"""
    body = hero + f"""
  <section class="tight">
    <div class="container contact-grid">
      <div class="reveal">{info_col}</div>
      <div class="reveal">{block_contact_form(lang)}</div>
    </div>
  </section>
"""
    html = page_shell(lang, base, "contact", lang_links_for("contact"),
                       f"{t['contact_title']} | {SITE['name']}", t['contact_lead'], body,
                       f"{SITE['domain']}/{lang}/contact.html")
    write(f"{lang}/contact.html", html)


def build_service_detail(service):
    """Detail pages live flat under /services/, rendered in Arabic (site's primary language)."""
    lang = "ar"
    base = "../"
    t = T[lang]
    title = service["title_ar"]
    desc = service["desc_ar"]
    bullets = service["bullets_ar"]
    lang_links = {"ar": f"../services/{service['slug']}.html", "en": "../en/services.html"}

    hero = f"""
  <section class="page-hero">
    <div class="container">
      <div class="breadcrumb"><a href="{base}ar/index.html">{NAV_PAGES[0][1]}</a><span>/</span><a href="{base}ar/services.html">{t['our_services']}</a><span>/</span><span>{title}</span></div>
      <div class="service-icon" style="margin-inline:auto">{ICONS[service['icon']]}</div>
      <h1 class="mt-2">{title}</h1>
      <p class="lead" style="margin-inline:auto">{t['service_detail_lead']}</p>
    </div>
  </section>
"""
    bullets_html = "".join(f"<li>{ICONS['check']}<span>{b}</span></li>" for b in bullets)
    about_section = f"""
  <section class="tight">
    <div class="container grid grid-2" style="align-items:center">
      <div class="reveal">
        <span class="eyebrow">{t['about_service']}</span>
        <h2 class="mt-1 mb-2">{title}</h2>
        <p class="lead mb-2">{desc}</p>
        <ul class="detail-list">{bullets_html}</ul>
      </div>
      <div class="reveal hero-frame">
        <img src="{base}assets/img/service-{service['slug']}.jpg" alt="{title}" loading="lazy" width="560" height="420">
      </div>
    </div>
  </section>
"""
    tech_map = {
        "web-development": ["Laravel", "PHP", "MySQL", "HTML5/CSS3", "JavaScript"],
        "laravel": ["Laravel", "PHP", "MySQL", "REST API", "Blade"],
        "wordpress": ["WordPress", "WooCommerce", "PHP", "MySQL"],
        "mobile-apps": ["Flutter", "Android", "Riverpod", "Firebase"],
        "ecommerce": ["Laravel", "WooCommerce", "Payment Gateways", "MySQL"],
        "ui-ux": ["Figma", "Adobe XD", "Prototyping", "Design Systems"],
    }
    tech_html = "".join(f'<span class="tech-pill">{x}</span>' for x in tech_map.get(service["slug"], []))
    tech_section = f"""
  <section class="tight">
    <div class="container text-center">
      <div class="section-head reveal"><span class="eyebrow">{t['tech_stack']}</span><h2>{t['tech_stack']}</h2></div>
      <div class="tech-pill-row reveal" style="justify-content:center">{tech_html}</div>
    </div>
  </section>
"""
    related = [p for p in PROJECTS if any(s.lower() in [x.lower() for x in p["stack"]] for s in tech_map.get(service["slug"], []))][:2] or PROJECTS[:2]
    _, related_grid = block_portfolio_grid(lang, base, projects=related)
    related_section = f"""
  <section class="tight">
    <div class="container">
      <div class="section-head reveal"><span class="eyebrow">{t['related_projects']}</span><h2>{t['related_projects']}</h2></div>
      {related_grid}
    </div>
  </section>
"""
    body = hero + about_section + tech_section + block_process(lang) + related_section + block_faq(lang) + block_cta(lang, base)
    html = page_shell(lang, base, None, lang_links, f"{title} | {SITE['name']}", desc, body,
                       f"{SITE['domain']}/services/{service['slug']}.html")
    write(f"services/{service['slug']}.html", html)


def build_project_detail(project):
    lang = "ar"
    base = "../"
    t = T[lang]
    title = project["title_ar"]
    lang_links = {"ar": f"../projects/{project['slug']}.html", "en": "../en/portfolio.html"}

    hero = f"""
  <section class="page-hero">
    <div class="container">
      <div class="breadcrumb"><a href="{base}ar/index.html">{NAV_PAGES[0][1]}</a><span>/</span><a href="{base}ar/portfolio.html">{t['portfolio_title']}</a><span>/</span><span>{title}</span></div>
      <h1 class="mt-1">{title}</h1>
      <p class="lead" style="margin-inline:auto">{project['summary_ar']}</p>
      <div class="project-links" style="justify-content:center">
        <a href="{project.get('live_demo')}" target="_blank" class="btn btn-primary btn-sm">{t['live_demo']} {ICONS['external']}</a>
        <a href="{project.get('github')}" target="_blank" class="btn btn-outline btn-sm">{ICONS['github']} GitHub</a>
      </div>
    </div>
  </section>
"""
    media = f"""
  <section class="tight" style="padding-top:0">
    <div class="container">
      <div class="project-hero-media reveal">
        <img src="{base}assets/img/project-{project['slug']}-cover.jpg" alt="{title}" loading="lazy" width="1200" height="700">
      </div>
    </div>
  </section>
"""
    tags = "".join(f'<span class="stack-tag">{s}</span>' for s in project["stack"])
    meta = f"""
  <section class="tight">
    <div class="container">
      <div class="project-meta-grid">
        <div class="glass-card meta-block reveal"><h4>{t['challenge']}</h4><p>{project['challenge_ar']}</p></div>
        <div class="glass-card meta-block reveal"><h4>{t['solution']}</h4><p>{project['solution_ar']}</p></div>
        <div class="glass-card meta-block reveal"><h4>{t['tech_stack']}</h4><div class="stack-tags">{tags}</div></div>
      </div>
      <div class="glass-card reveal mt-3">
        <h3 class="mb-2">{t['features']}</h3>
        <ul class="detail-list">{''.join(f"<li>{ICONS['check']}<span>{f}</span></li>" for f in project['features_ar'])}</ul>
      </div>
    </div>
  </section>
"""
    others = [p for p in PROJECTS if p["slug"] != project["slug"]][:2]
    _, others_grid = block_portfolio_grid(lang, base, projects=others)
    others_section = f"""
  <section class="tight">
    <div class="container">
      <div class="section-head reveal"><span class="eyebrow">{t['related_projects']}</span><h2>{t['related_projects']}</h2></div>
      {others_grid}
      <div class="text-center mt-3"><a href="{base}ar/portfolio.html" class="btn btn-outline">{t['back_to_portfolio']}</a></div>
    </div>
  </section>
"""
    body = hero + media + meta + others_section + block_cta(lang, base)
    html = page_shell(lang, base, None, lang_links, f"{title} | {SITE['name']}", project["summary_ar"], body,
                       f"{SITE['domain']}/projects/{project['slug']}.html")
    write(f"projects/{project['slug']}.html", html)


def build_legal_page(kind):
    lang = "ar"
    base = ""
    t = T[lang]
    is_privacy = kind == "privacy"
    title = t["privacy"] if is_privacy else t["terms"]
    lang_links = {"ar": f"{kind}.html", "en": "en/index.html"}

    if is_privacy:
        content = """
        <p>نحن في NOVIX نولي خصوصيتك أهمية كبيرة، وتوضح هذه السياسة كيفية جمعنا واستخدامنا وحمايتنا لبياناتك عند استخدام موقعنا وخدماتنا.</p>
        <h2>المعلومات التي نجمعها</h2>
        <ul>
          <li>بيانات التواصل مثل الاسم والبريد الإلكتروني ورقم الهاتف عند تعبئة نموذج التواصل.</li>
          <li>تفاصيل المشروع التي تشاركها معنا لتقديم عرض سعر مناسب.</li>
          <li>بيانات تصفح عامة وغير شخصية لتحسين أداء الموقع.</li>
        </ul>
        <h2>كيفية استخدام بياناتك</h2>
        <ul>
          <li>الرد على استفساراتك وطلبات التواصل.</li>
          <li>تقديم عروض أسعار ومتابعة تنفيذ مشاريعك.</li>
          <li>تحسين خدماتنا وتجربة استخدام الموقع.</li>
        </ul>
        <h2>حماية البيانات</h2>
        <p>نتخذ إجراءات تقنية وتنظيمية معقولة لحماية بياناتك من الوصول غير المصرح به أو الفقدان أو سوء الاستخدام.</p>
        <h2>التواصل معنا</h2>
        <p>لأي استفسار بخصوص سياسة الخصوصية، يمكنك التواصل معنا عبر البريد الإلكتروني الموضح في صفحة التواصل.</p>
"""
    else:
        content = """
        <p>باستخدامك لموقع NOVIX وخدماتنا، فإنك توافق على الشروط والأحكام التالية.</p>
        <h2>نطاق الخدمات</h2>
        <ul>
          <li>تقدم NOVIX خدمات تصميم وتطوير المواقع والتطبيقات وفق نطاق يُتفق عليه مسبقًا مع كل عميل.</li>
          <li>أي تعديل على نطاق العمل بعد الاتفاق قد يستلزم مراجعة السعر والجدول الزمني.</li>
        </ul>
        <h2>الدفع والتسليم</h2>
        <ul>
          <li>يتم الاتفاق على آلية الدفع والجدول الزمني للتسليم قبل بدء العمل.</li>
          <li>يلتزم الطرفان بالمواعيد المتفق عليها إلا في حال وجود ظروف استثنائية يتم إخطار العميل بها.</li>
        </ul>
        <h2>الملكية الفكرية</h2>
        <p>تنتقل ملكية العمل النهائي إلى العميل بعد استكمال السداد بالكامل، ما لم يُتفق على خلاف ذلك كتابيًا.</p>
        <h2>التعديلات</h2>
        <p>تحتفظ NOVIX بحق تحديث هذه الشروط من وقت لآخر، وسيتم نشر أي تحديثات على هذه الصفحة.</p>
"""
    hero = f"""
  <section class="page-hero">
    <div class="container">
      <div class="breadcrumb"><a href="{base}ar/index.html">{NAV_PAGES[0][1]}</a><span>/</span><span>{title}</span></div>
      <h1 class="mt-1">{title}</h1>
    </div>
  </section>
"""
    body = hero + f'<section class="tight"><div class="container legal-content">{content}</div></section>'
    html = page_shell(lang, base, None, lang_links, f"{title} | {SITE['name']}",
                       "سياسة الخصوصية والشروط والأحكام الخاصة بموقع NOVIX", body, f"{SITE['domain']}/{kind}.html")
    write(f"{kind}.html", html)


def build_root_index():
    """Root index.html redirects visitors to the Arabic homepage (default site language)."""
    html = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta http-equiv="refresh" content="0; url=ar/index.html">
<link rel="canonical" href="ar/index.html">
<title>NOVIX</title>
</head>
<body>
<p>Redirecting to <a href="ar/index.html">NOVIX</a>...</p>
</body>
</html>
"""
    write("index.html", html)


# ------------------------------------------------------------------ #
# Build everything
# ------------------------------------------------------------------ #

def main():
    for lang in ("ar", "en"):
        build_home(lang)
        build_services_page(lang)
        build_portfolio_page(lang)
        build_about_page(lang)
        build_contact_page(lang)

    for s in SERVICES:
        build_service_detail(s)

    for p in PROJECTS:
        build_project_detail(p)

    build_legal_page("privacy")
    build_legal_page("terms")
    build_root_index()

    print("\nAll pages generated successfully.")


if __name__ == "__main__":
    main()
