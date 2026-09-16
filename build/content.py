# -*- coding: utf-8 -*-
"""
Eshop niche content for seopreeshopy.pro (SK + CZ).

Keywords grounded in Marketing Miner (2026-09):
CZ seo optimalizace eshopu 490 (diff 34), seo eshop 430 (diff 35),
seo eshopu 350 (diff 47). SK eshop seo 30, seo eshop 20.
"""

from engine import _VIOLET, _ORANGE, _CERULEAN, _VIOLET_L, _sparkline, _bars

SERVICE_DEFS = [
    ("sluzby/seo-optimalizacia/", "sluzby/seo-optimalizace/",
     "SEO optimalizácia e-shopu", "SEO optimalizace e-shopu"),
    ("sluzby/kategorie-a-produkty/", "sluzby/kategorie-a-produkty/",
     "Kategórie a produktové stránky", "Kategorie a produktové stránky"),
    ("sluzby/technicke-seo-eshopu/", "sluzby/technicke-seo-eshopu/",
     "Technické SEO e-shopu", "Technické SEO e-shopu"),
    ("sluzby/eshop-audit/", "sluzby/eshop-audit/",
     "SEO audit e-shopu", "SEO audit e-shopu"),
]
SERVICE_DEFS_TEXT = [
    ("Celý e-shop nastavím tak, aby Google aj AI nástroje vašim produktom rozumeli: štruktúra, popisy, interné odkazy.",
     "Celý e-shop nastavím tak, aby Google i AI nástroje vašim produktům rozumely: struktura, popisy, interní odkazy."),
    ("Kategórie a produkty optimalizujem na kľúčové slová, ktoré kupujú. Viac predaja z existujúceho e-shopu, nie viac návštevnosti.",
     "Kategorie a produkty optimalizuji na klíčová slova, která kupují. Více prodeje z existujícího e-shopu, ne více návštěvnosti."),
    ("Filtrácia, farebné a veľkostné varianty, XML feedy, rýchlosť. Technika, ktorá rozhoduje o tom, či Google zobrazí správny variant.",
     "Filtrování, barevné a velikostní varianty, XML feedy, rychlost. Technika, která rozhoduje o tom, zda Google zobrazí správnou variantu."),
    ("Presný obraz toho, čo brzdí váš e-shop: 15-bodová kontrola s plánom podľa priorít a odhadom hodín.",
     "Přesný obraz toho, co brzdí váš e-shop: 15-bodová kontrola s plánem podle priorit a odhadem hodin."),
]
SERVICE_DEFS_ICON = ["shop", "target", "bolt", "audit"]
SERVICE_DEFS_COLOR = ["#1DACD6", "#6A3FC4", "#F75940", "#6A3FC4"]
SERVICE_DEFS_TAG = ["tag-cerulean", "tag-violet", "tag-orange", "tag-violet-light"]

SLIDES = [
    {"client": "E-shop (vlastný projekt)", "chip": "AI viditeľnosť",
     "period": "Google AI Mode, jún až september 2026",
     "nums": [{"big": "893", "color": _VIOLET_L, "label": "zobrazení v AI Mode za 3 mesiace"},
              {"big": "+80 %", "color": _VIOLET, "label": "august oproti júnu (182 → 329)"},
              {"big": "174", "color": _CERULEAN, "label": "citácií homepage"}],
     "chart": _bars([182, 293, 329, 413], _VIOLET_L, ["jún", "júl", "aug", "sep"]),
     "caption": "Google AI Mode cituje e-shop denne po nasadení môjho obsahu. Rast mesačne: jún 182, júl 293, august 329. Najviac citované: homepage a blogové články. Konkurencia v AI odpovediach ešte nie je.",
     "logo": "speem.webp"},
    {"client": "E-shop so školskými pomôckami", "chip": "Eshop SEO + email",
     "period": "9 mesiacov",
     "nums": [{"big": "2 492 EUR", "color": _VIOLET, "label": "tržby za 9 mesiacov"},
              {"big": "15", "color": _ORANGE, "label": "objednávok z e-mailu a organika"},
              {"big": "722 EUR", "color": _CERULEAN, "label": "najväčšia objednávka"}],
     "chart": _sparkline([10, 14, 12, 18, 22, 26, 31, 38, 44], _VIOLET),
     "caption": "Vlastný e-shop s API integráciou na účtovný systém. Tržby pripísané kanálom e-mail a organické vyhľadávanie Google."},
]

PROCESS = {
    "sk": {
        "s1_t": "Bezplatný audit e-shopu", "s1_x": "Začneme 30-minútovým hovorom a bezplatným auditom. Pozrieme kategórie, produkty, techniku aj to, čo Google o vašom e-shope vidí.",
        "s2_t": "Plán podľa priorít", "s2_x": "Kategórie s najväčším predajným potenciálom ako prvé, produkty s objemom hľadania, koľko hodín mesačne to zaberie.",
        "s3_t": "Práca v týždenných dávkach", "s3_x": "Kategórie, produkty, technika, obsah. Vždy viete, čo sa stalo v predchádzajúcom týždni a čo nasleduje.",
        "s4_t": "Meranie a report", "s4_x": "Mesačný report vám dám osobne: 30-minútový telefonát. Pozície, kliky, objednávky z organiku. Platíte len za odpracované hodiny.",
    },
    "cz": {
        "s1_t": "Bezplatný audit e-shopu", "s1_x": "Začneme 30minutovým hovorem a bezplatným auditem. Podíváme se na kategorie, produkty, techniku i na to, co Google o vašem e-shopu vidí.",
        "s2_t": "Plán podle priorit", "s2_x": "Kategorie s největším prodejním potenciálem jako první, produkty s objemem hledání, kolik hodin měsíčně to zabere.",
        "s3_t": "Práce v týdenních dávkách", "s3_x": "Kategorie, produkty, technika, obsah. Vždy víte, co se stalo v předchozím týdnu a co následuje.",
        "s4_t": "Měření a report", "s4_x": "Měsíční report vám dám osobně: 30minutový telefonát. Pozice, kliky, objednávky z organiku. Platíte jen za odpracované hodiny.",
    },
}

FAQ = {
    "sk": {
        "common": [
            ("Koľko stojí SEO pre e-shop?",
             "Za prácu platíte 12 EUR za hodinu. Menší e-shop zvládnem za 20 hodín mesačne (240 EUR), väčší za 40 hodín (480 EUR). Presný rozsah vám potvrdím v pláne po bezplatnom audite."),
            ("Ako dlho trvá, kým e-shop SEO prinesie predaje?",
             "Prvé objednávky z dlhšieho chvosta (kategórie, produktové frázy) zvyčajne za 2 až 4 mesiace. Hlavné kategórie trvajú 6 až 12 mesiacov. Reálne termíny vám poviem už v audite."),
            ("Pracujete aj so Shoptet a Upgates?",
             "Áno. Shoptet, Upgates a WooCommerce sú najčastejšie platformy, s ktorými pracujem. Vedia ako štruktúrovať kategórie aj produkty v ich systémoch."),
            ("Optimalizujete aj produktové feedy?",
             "Áno, XML feedy pre Google Merchant Center sú súčasťou práce: správne názvy, popisy, atribúty a dostupnosť."),
            ("Čo ak mám e-shop aj na Heureke?",
             "Google a Heureka sú dva kanály. Ja riešim Google aj to, aby vás AI nástroje (ChatGPT, Gemini) odporúčali. Heureka optimalizáciu riešim ako doplnok."),
        ],
        "sluzby": [
            ("Ktoré e-shopy riešite ako prvé?", "Kategórie s najväčším objemom hľadania a najlepšou maržou. Produkty s dlhším chvostom potom, keď kategórie stoja."),
            ("Robíte aj obsah pre blog e-shopu?", "Áno. Blog e-shopu je najrýchlejšia cesta k informácií hľadaniu. Píšem články na kľúčové slová, ktoré zákazníci hľadajú pred nákupom."),
        ],
        "cennik": [
            ("Prečo hodinová cena a nie paušál?", "Lebo viete presne, za čo platíte. E-shopové SEO je práca po dávkach, nie paušál. Každá hodina je vykázaná."),
            ("Koľko hodín potrebuje e-shop mesačne?", "Menší e-shop 20 hodín (240 EUR), stredný 30 hodín, veľký 40 hodín a viac. Spresní to plán po audite."),
        ],
        "proces": [
            ("Do akého e-shopu sa pripojím?", "Potrebujem účet s právami na úpravu stránok a produktov. Pracujem aj cez staging, ak ho máte."),
            ("Čo ak má e-shop veľa produktov?", "Produkty riešim systémovo: šablóny popisov, pravidlá pre varianty, feedy. Neoptimalizujem 5000 produktov ručne."),
        ],
    },
    "cz": {
        "common": [
            ("Kolik stojí SEO pro e-shop?",
             "Za práci platíte 12 EUR za hodinu. Menší e-shop zvládnu za 20 hodin měsíčně (240 EUR), větší za 40 hodin (480 EUR). Přesný rozsah potvrdím v plánu po bezplatném auditu."),
            ("Jak dlouho trvá, než e-shop SEO přinese prodeje?",
             "První objednávky z delšího chvostu (kategorie, produktové fráze) zpravidla za 2 až 4 měsíce. Hlavní kategorie trvají 6 až 12 měsíců. Reálné termíny vám řeknu už v auditu."),
            ("Pracujete i se Shoptet a Upgates?",
             "Ano. Shoptet, Upgates a WooCommerce jsou nejčastější platformy, se kterými pracuji. Umím strukturovat kategorie i produkty v jejich systémech."),
            ("Optimalizujete i produktové feedy?",
             "Ano, XML feedy pro Google Merchant Center jsou součástí práce: správné názvy, popisy, atributy a dostupnost."),
            ("Co když mám e-shop i na Heurece?",
             "Google a Heureka jsou dva kanály. Já řeším Google i to, aby vás AI nástroje (ChatGPT, Gemini) doporučovaly. Heureka optimalizaci řeším jako doplněk."),
        ],
        "sluzby": [
            ("Které e-shopy řešíte jako první?", "Kategorie s největším objemem hledání a nejlepší marží. Produkty s delším chvostem potom, když kategorie stojí."),
            ("Děláte i obsah pro blog e-shopu?", "Ano. Blog e-shopu je nejrychlejší cesta k informacím ve vyhledávání. Píšu články na klíčová slova, která zákazníci hledají před nákupem."),
        ],
        "cennik": [
            ("Proč hodinová cena a ne paušál?", "Protože víte přesně, za co platíte. E-shopové SEO je práce po dávkách, ne paušál. Každá hodina je vykázaná."),
            ("Kolik hodin potřebuje e-shop měsíčně?", "Menší e-shop 20 hodin (240 EUR), střední 30 hodin, velký 40 hodin a více. Spřesní to plán po auditu."),
        ],
        "proces": [
            ("Do jakého e-shopu se připojím?", "Potřebuji účet s právy na úpravu stránek a produktů. Pracuji i přes staging, pokud ho máte."),
            ("Co když má e-shop mnoho produktů?", "Produkty řeším systémově: šablony popisů, pravidla pro varianty, feedy. Neoptimalizuji 5000 produktů ručně."),
        ],
    },
}

DETAIL = [
    {  # 0: seo-optimalizacia eshopu
        "sk": {
            "h1": 'SEO optimalizácia e-shopu: nech vás zákazníci nájdu v <span class="hl-violet">Google</span>',
            "sub": "Celý e-shop nastavím tak, aby Google vašim kategóriám aj produktom rozumel. Bez platenej reklamy, s predajom z organiku.",
            "title": "SEO optimalizácia e-shopu | SEO pre e-shopy",
            "desc": "SEO optimalizácia e-shopu za 12 EUR za hodinu. Kategórie, produkty, technika a obsah. Nokto Studio, SEO špecialista pre e-shopy.",
            "b1_t": "Čo nastavím", "b1_x": "Štruktúru kategórií, meta údaje, popisy produktov a kategórií, interné odkazy, riešenie duplicit a kanonických URL.",
            "b2_t": "Čo dostanete", "b2_x": "E-shop, ktorý Google radí na kľúčové slová, ktoré zákazníci hľadajú pred nákupom. Viac objednávok z organiku, nielen návštevnosť.",
            "what_t": "Ako SEO e-shopu prebieha",
            "what_x": "Pracujem priamo vo vašom eshopovom systéme (Shoptet, Upgates, WooCommerce). Každá zmena je popísaná v reporte.",
        },
        "cz": {
            "h1": 'SEO optimalizace e-shopu: nech vás zákazníci najdou v <span class="hl-violet">Google</span>',
            "sub": "Celý e-shop nastavím tak, aby Google vašim kategoriím i produktům rozumel. Bez placené reklamy, s prodejem z organiku.",
            "title": "SEO optimalizace e-shopu | SEO pro e-shopy",
            "desc": "SEO optimalizace e-shopu za 12 EUR za hodinu. Kategorie, produkty, technika a obsah. Nokto Studio, SEO specialista pro e-shopy.",
            "b1_t": "Co nastavím", "b1_x": "Strukturu kategorií, meta údaje, popisy produktů a kategorií, interní odkazy, řešení duplicit a kanonických URL.",
            "b2_t": "Co dostanete", "b2_x": "E-shop, který Google řadí na klíčová slova, která zákazníci hledají před nákupem. Více objednávek z organiku, ne jen návštěvnost.",
            "what_t": "Jak SEO e-shopu probíhá",
            "what_x": "Pracuji přímo ve vašem eshopovém systému (Shoptet, Upgates, WooCommerce). Každá změna je popsána v reportu.",
        },
    },
    {  # 1: kategorie-a-produkty
        "sk": {
            "h1": 'Kategórie a produkty, ktoré <span class="hl-orange">predávajú</span> z Google',
            "sub": "Kategórie sú najväčší eshop SEO kanál. Produkty s dlhším chvostom potom prinesú objednávky skôr, než čakáte.",
            "title": "SEO pre kategórie a produktové stránky e-shopu | SEO pre e-shopy",
            "desc": "Optimalizácia kategórií a produktových stránok e-shopu na kľúčové slová, ktoré kupujú. Nokto Studio, 12 EUR za hodinu.",
            "b1_t": "Čo robím s kategóriami", "b1_x": "Texty kategórií na reálne hľadania, správne nadpisy, filtre bez duplicit a interné odkazy medzi kategóriami a blogom.",
            "b2_t": "Čo robím s produktmi", "b2_x": "Popisy na produktové frázy (farba, veľkosť, model), správne varianty a dostupnosť vo feedoch pre Google Shopping.",
            "what_t": "Systém, nie ručná práca",
            "what_x": "Veľké e-shopy neoptimalizujem produkt po produkte. Nastavím pravidlá a šablóny, ktoré fungujú na celú rodinu produktov.",
        },
        "cz": {
            "h1": 'Kategorie a produkty, které <span class="hl-orange">prodávají</span> z Google',
            "sub": "Kategorie jsou největší eshop SEO kanál. Produkty s delším chvostem potom přinesou objednávky dřív, než čekáte.",
            "title": "SEO pro kategorie a produktové stránky e-shopu | SEO pro e-shopy",
            "desc": "Optimalizace kategorií a produktových stránek e-shopu na klíčová slova, která kupují. Nokto Studio, 12 EUR za hodinu.",
            "b1_t": "Co dělám s kategoriemi", "b1_x": "Texty kategorií na reálná hledání, správné nadpisy, filtry bez duplicit a interní odkazy mezi kategoriemi a blogem.",
            "b2_t": "Co dělám s produkty", "b2_x": "Popisy na produktové fráze (barva, velikost, model), správné varianty a dostupnost ve feedech pro Google Shopping.",
            "what_t": "Systém, ne ruční práce",
            "what_x": "Velké e-shopy neoptimalizuji produkt po produktu. Nastavím pravidla a šablony, které fungují na celou rodinu produktů.",
        },
    },
    {  # 2: technicke-seo-eshopu
        "sk": {
            "h1": 'Technické SEO e-shopu: <span class="hl-cerulean-light">rýchlosť</span>, varianty a feedy',
            "sub": "Filtrácia, farebné a veľkostné varianty, XML feedy, rýchlosť. Technika, ktorá rozhoduje o tom, čo Google z e-shopu vidí.",
            "title": "Technické SEO e-shopu | SEO pre e-shopy",
            "desc": "Technické SEO e-shopu: rýchlosť, filtre, varianty produktov, XML feedy pre Google Shopping. Nokto Studio, 12 EUR za hodinu.",
            "b1_t": "Čo riešim", "b1_x": "Duplicitné URL z filtrov, kanonické adresy, rýchlosť načítania, štruktúrované dáta produktov a XML feedy pre Merchant Center.",
            "b2_t": "Prečo to rozhoduje", "b2_x": "Google zobrazuje len čisté adresy bez duplicit. Ak filtre vytvárajú tisíce duplicitných URL, Google stráca rozsah a e-shop stojí.",
            "what_t": "Ako technika e-shopu prebieha",
            "what_x": "Začnem crawlom a Search Console. Potom opravy v eshopovom systéme, hostingu a feedoch. Väčšina sa dá urobiť bez programátora.",
        },
        "cz": {
            "h1": 'Technické SEO e-shopu: <span class="hl-cerulean-light">rychlost</span>, varianty a feedy',
            "sub": "Filtrování, barevné a velikostní varianty, XML feedy, rychlost. Technika, která rozhoduje o tom, co Google z e-shopu vidí.",
            "title": "Technické SEO e-shopu | SEO pro e-shopy",
            "desc": "Technické SEO e-shopu: rychlost, filtry, varianty produktů, XML feedy pro Google Shopping. Nokto Studio, 12 EUR za hodinu.",
            "b1_t": "Co řeším", "b1_x": "Duplicitní URL z filtrů, kanonické adresy, rychlost načítání, strukturovaná data produktů a XML feedy pro Merchant Center.",
            "b2_t": "Proč to rozhoduje", "b2_x": "Google zobrazuje jen čisté adresy bez duplicit. Když filtry vytvářejí tisíce duplicitních URL, Google ztrácí rozsah a e-shop stojí.",
            "what_t": "Jak technika e-shopu probíhá",
            "what_x": "Začnu crawlem a Search Console. Potom opravy v eshopovém systému, hostingu a feedech. Většina jde udělat bez programátora.",
        },
    },
    {  # 3: eshop-audit
        "sk": {
            "h1": '<span class="hl-violet-light">SEO audit</span> e-shopu: čo brzdí vaše predaje v Google',
            "sub": "Presný obraz: ktoré kategórie stoja, kde stráca technika, čo chýba produktom. Bezplatný audit ako prvý krok.",
            "title": "SEO audit e-shopu | SEO pre e-shopy",
            "desc": "SEO audit e-shopu: 15-bodová kontrola kategórií, produktov, techniky a pozícií. Bezplatný vstupný audit. Nokto Studio.",
            "b1_t": "Čo audítom zistím", "b1_x": "Ktoré kategórie Google vidí, kde strácajú pozície, čo brzdí produkty, či filtre vytvárajú duplicity a čo chýba vo feede.",
            "b2_t": "Ako audit vyzerá", "b2_x": "15-bodová kontrola so zoznamom opráv podľa priorít a odhadom hodín. Bezplatný vstupný audit robím pred prvou faktúrou.",
            "what_t": "Po audite",
            "what_x": "Dostanete plán: ktoré kategórie riešiť ako prvé, koľko hodín mesačne a čo môžete očakávať. Rozhodnutie je vaše, bez záväzku.",
        },
        "cz": {
            "h1": '<span class="hl-violet-light">SEO audit</span> e-shopu: co brzdí vaše prodeje v Google',
            "sub": "Přesný obraz: které kategorie stojí, kde ztrácí technika, co chybí produktům. Bezplatný audit jako první krok.",
            "title": "SEO audit e-shopu | SEO pro e-shopy",
            "desc": "SEO audit e-shopu: 15 bodová kontrola kategorií, produktů, techniky a pozic. Bezplatný vstupní audit. Nokto Studio.",
            "b1_t": "Co auditem zjistím", "b1_x": "Které kategorie Google vidí, kde ztrácejí pozice, co brzdí produkty, zda filtry vytvářejí duplicity a co chybí ve feedu.",
            "b2_t": "Jak audit vypadá", "b2_x": "15 bodová kontrola se seznamem oprav podle priorit a odhadem hodin. Bezplatný vstupní audit dělám před první fakturou.",
            "what_t": "Po auditu",
            "what_x": "Dostanete plán: které kategorie řešit jako první, kolik hodin měsíčně a co můžete očekávat. Rozhodnutí je vaše, bez závazku.",
        },
    },
]

DETAIL_FAQ = {
    0: {
        "sk": [("Pracujete aj s platformami ako PrestaShop?", "Áno, pracujem so všetkými hlavnými platformami. Čo presne sa dá zmeniť, vám povedané pri audite."),
               ("Ako rýchlo uvidím prvé objednávky?", "Dlhší chvost (produktové frázy s farbou a modelom) zvyčajne 2 až 4 mesiace. Hlavné kategórie 6 až 12 mesiacov.")],
        "cz": [("Pracujete i s platformami jako PrestaShop?", "Ano, pracuji se všemi hlavními platformami. Co přesně jde změnit, vám řeknu při auditu."),
               ("Jak rychle uvidím první objednávky?", "Delší chvost (produktové fráze s barvou a modelem) zpravidla 2 až 4 měsíce. Hlavní kategorie 6 až 12 měsíců.")],
    },
    1: {
        "sk": [("Píšete aj texty kategórií?", "Áno, texty kategórií píšem na reálne hľadania z dát, nie na generické frázy. Každá kategória má plán."),
               ("Čo ak mám 5000 produktov?", "Nastavím šablóny a pravidlá, ktoré pokrývajú celú rodinu produktov. Ručná práca len tam, kde sa vypláca.")],
        "cz": [("Píšete i texty kategorií?", "Ano, texty kategorií píšu na reálná hledání z dat, ne na generické fráze. Každá kategorie má plán."),
               ("Co když mám 5000 produktů?", "Nastavím šablony a pravidla, které pokrývají celou rodinu produktů. Ruční práce jen tam, kde se vyplácí.")],
    },
    2: {
        "sk": [("Riešite aj Google Merchant Center?", "Áno, XML feedy a Merchant Center sú súčasť technickej práce. Správne atribúty, dostupnosť a ceny."),
               ("Musím meniť eshopový systém?", "Nemusí. Väčšina technických opráv sa dá urobiť v nastaveniach platformy. Čo nie, vám povedané priamo.")],
        "cz": [("Řešíte i Google Merchant Center?", "Ano, XML feedy a Merchant Center jsou součástí technické práce. Správné atributy, dostupnost a ceny."),
               ("Musím měnit eshopový systém?", "Nemusí. Většina technických oprav jde udělat v nastaveních platformy. Co ne, vám řeknu přímo.")],
    },
    3: {
        "sk": [("Je audit skutočne bezplatný?", "Áno. Audit a 30-minútový hovor sú bezplatné, bez záväzku. Platíte až za samotnú prácu po pláne."),
               ("Čo dostanem v audite?", "Zoznam 15 bodov s prioritami, odhadom hodín a predpokladaným efektom. Bez technickej reči, ktorá nevraví nič.")],
        "cz": [("Je audit skutečně bezplatný?", "Ano. Audit a 30minutový hovor jsou bezplatné, bez závazku. Platíte až za samotnou práci po plánu."),
               ("Co dostanu v auditu?", "Seznam 15 bodů s prioritami, odhadem hodin a předpokládaným efektem. Bez technické řeči, která neříká nic.")],
    },
}

BLOG_POSTS = {
    "sk": [
        {"href": "blog/seo-pre-eshop-navod/", "title": "SEO pre e-shop: návod krok za krokom (2026)",
         "desc": "Ako nastaviť e-shop pre Google: kategórie, produkty, technika a obsah. Bez zbytočnej technickej reči.", "tag": "Návod"},
        {"href": "blog/kategorie-seo/", "title": "Kategórie e-shopu: ako ich optimalizovať pre Google",
         "desc": "Kategórie sú najväčší SEO kanál e-shopu. Ako ich štruktúrovať a písať texty, ktoré predávajú.", "tag": "Kategórie"},
        {"href": "blog/shoptet-seo/", "title": "SEO na Shoptet: čo nastaviť a čo riešiť systémovo",
         "desc": "Shoptet má svoje pravidlá. Čo sa dá nastaviť v adminovi a čo vyžaduje zásah šablóny.", "tag": "Shoptet"},
        {"href": "blog/eshop-seo-cena/", "title": "Koľko stojí SEO pre e-shop a čo za to dostanete",
         "desc": "Hodinová cena vs paušál. Čo je reálne v cene a čo nie. Koľko hodín potrebuje e-shop mesačne.", "tag": "Cena"},
    ],
    "cz": [
        {"href": "blog/seo-pre-eshop-navod/", "title": "SEO pro e-shop: návod krok za krokem (2026)",
         "desc": "Jak nastavit e-shop pro Google: kategorie, produkty, technika a obsah. Bez zbytečné technické řeči.", "tag": "Návod"},
        {"href": "blog/kategorie-seo/", "title": "Kategorie e-shopu: jak je optimalizovat pro Google",
         "desc": "Kategorie jsou největší SEO kanál e-shopu. Jak je strukturovat a psát texty, které prodávají.", "tag": "Kategorie"},
        {"href": "blog/shoptet-seo/", "title": "SEO na Shoptet: co nastavit a co řešit systémově",
         "desc": "Shoptet má svá pravidla. Co se dá nastavit v adminu a co vyžaduje zásah šablony.", "tag": "Shoptet"},
        {"href": "blog/eshop-seo-cena/", "title": "Kolik stojí SEO pro e-shop a co za to dostanete",
         "desc": "Hodinová cena vs paušál. Co je reálně v ceně a co ne. Kolik hodin potřebuje e-shop měsíčně.", "tag": "Cena"},
    ],
}
