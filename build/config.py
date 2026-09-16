# -*- coding: utf-8 -*-
"""
Eshop niche configuration for seopreeshopy.pro, then run
`python3 build_site.py` from the repo root.

Keywords grounded in Marketing Miner data (2026-09):
CZ: seo optimalizace eshopu 490, seo eshop 430, seo eshopu 350.
SK: eshop seo 30, seo eshop 20 (low volume, low competition).
"""
import engine

BASE = "https://seopreeshopy.pro"
BRAND = "SEO pre e-shopy"
BRAND_TAGLINE = "SEO optimalizácia e-shopov. Nokto Studio."

NICHE_KEY = "eshop"
MAIN_DOMAIN = "seopreeshopy.pro"

KW_PROOF_SK = [
    ("eshop seo", 30),
    ("seo eshop", 20),
    ("seo služby", 290),
    ("seo optimalizácia", 490),
]
KW_PROOF_CZ = [
    ("seo optimalizace eshopu", 490),
    ("seo eshop", 430),
    ("seo eshopu", 350),
    ("seo optimalizace e-shopu", 140),
]

SERVICES = [
    ("sluzby/seo-optimalizacia/", "sluzby/seo-optimalizace/",
     "SEO optimalizácia e-shopu", "SEO optimalizace e-shopu"),
    ("sluzby/kategorie-a-produkty/", "sluzby/kategorie-a-produkty/",
     "Kategórie a produktové stránky", "Kategorie a produktové stránky"),
    ("sluzby/technicke-seo-eshopu/", "sluzby/technicke-seo-eshopu/",
     "Technické SEO e-shopu", "Technické SEO e-shopu"),
    ("sluzby/eshop-audit/", "sluzby/eshop-audit/",
     "SEO audit e-shopu", "SEO audit e-shopu"),
]

NICHE_NAV_SVC = {
    "sk": [(p_sk, lbl_sk) for (p_sk, _p_cz, lbl_sk, _lbl_cz) in SERVICES],
    "cz": [(p_cz, lbl_cz) for (_p_sk, p_cz, _lbl_sk, lbl_cz) in SERVICES],
}
engine.NICHE_NAV_SVC = NICHE_NAV_SVC

SK_PATHS = {
    "", "sluzby/", "cennik/", "jak-pracujeme/", "blog/", "kontakt/",
    "privacy/", "terms/",
} | {s[0] for s in SERVICES}
CZ_PATHS = {
    "", "sluzby/", "cenik/", "jak-pracujeme/", "blog/", "kontakt/",
    "privacy/", "terms/",
} | {s[1] for s in SERVICES}
engine.LANG_PATHS = {"sk": SK_PATHS, "cz": CZ_PATHS}

HREFLANG_PAIR = {
    "": "",
    "sluzby/": "sluzby/",
    "cennik/": "cenik/",
    "jak-pracujeme/": "jak-pracujeme/",
    "blog/": "blog/",
    "kontakt/": "kontakt/",
    "privacy/": "privacy/",
    "terms/": "terms/",
}
for s in SERVICES:
    HREFLANG_PAIR[s[0]] = s[1]
    HREFLANG_PAIR[s[1]] = s[0]
engine.HREFLANG_PAIR = HREFLANG_PAIR

engine.BASE = BASE
engine.BRAND = BRAND
engine.LOGO = ('<span class="logo-n">S</span><span class="logo-o">E</span>'
               '<span class="logo-k">O</span> <span class="logo-t">eshop</span>')

engine.GSC_TOKEN = ""
engine.BING_TOKEN = "3b43ea1af0ee49f082ab3c4e94ed5f4f"
