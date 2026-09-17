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


# ---------------------------------------------------------------- blog articles
BLOG_ARTICLES = {
    "seo-pre-eshop-navod": {
        "sk": {
            "label": "Návod",
            "h1": "SEO pre e-shop: kompletný návod 2026",
            "title": "SEO pre e-shop: kompletný návod 2026 | SEO pre e-shopy",
            "desc": "SEO pre e-shop krok za krokom: kategórie, produkty, technika a obsah. Návod s reálnymi číslami a cenami od 240 EUR mesačne.",
            "date_display": "17. 9. 2026", "date_iso": "2026-09-17",
            "answer": "SEO pre e-shop je optimalizácia kategórií a produktov na dopyty, ktoré zákazníci hľadajú pred nákupom. Štruktúra kategórií, systémové popisy produktov, riešenie filtrov a XML feedy pre Google Shopping. Prvé objednávky z dlhšieho chvosta za 2 až 4 mesiace, cena od 240 EUR mesačne (12 EUR za hodinu).",
            "sections": """
<h2>Prečo e-shopy potrebujú iné SEO než firemné weby</h2>
<p>E-shop má tisíce stránok, filtrovanie a varianty. Google musí rozumieť, ktorá URL je správna pre ktorý dopyt. Presne preto e-shop SEO začína technikou: duplicitné URL z filtrov, kanonické adresy, štruktúrované dáta produktov. Firemný web má 10 stránok, e-shop 10 000. Každá chyba sa násobí.</p>

<h2>Krok 1: Kategórie ako hlavný SEO kanál</h2>
<p>Kategórie sú stránky, ktoré Google radí na hlavné dopyty: topánky na behanie, školské tašky. Každá kategória potrebuje: text na reálne hľadania, správny H1, interné odkazy a filtre bez duplicitných URL. Dopyty overte cez Marketing Miner alebo autocomplete.</p>

<h2>Krok 2: Produkty systémovo, nie ručne</h2>
<p>Nemôžete optimalizovať 5 000 produktov jeden po druhom. Nastavte šablóny popisov a pravidlá: farba + model + použitie v názve, dostupnosť v feede, varianty správne označené. Ručná práca len tam, kde sa vypláca (najpredávanejšie produkty).</p>

<h2>Krok 3: Technika a feedy</h2>
<ul>
<li><strong>Filre</strong>: žiadne duplicitné URL, canonical na čistú adresu.</li>
<li><strong>XML feed</strong>: Google Merchant Center s správnymi atribútmi (názov, cena, dostupnosť, GTIN).</li>
<li><strong>Rýchlosť</strong>: LCP pod 2,5 s. E-shopy sú ťažké, cache a WebP sú povinnosť.</li>
<li><strong>Schema</strong>: Product + Offer + Review. Google zobrazuje ceny a hodnotenia priamo v SERP.</li>
</ul>

<h2>Koľko SEO pre e-shop stojí</h2>
<p>Menší e-shop: 20 hodín mesačne = 240 EUR. Stredný e-shop (kategórie + produkty + obsah): 30 hodín = 360 EUR. Veľký e-shop so systémovou optimalizáciou: 40 hodín = 480 EUR. Prvá hodina je bezplatný audit e-shopu, aby ste videli, čo brzdí váš predaj.</p>
""",
            "faq": [
                ("Ako dlho trvá, kým e-shop SEO prinesie objednávky?", "Dlhší chvost (produktové frázy s farbou a modelom) 2 až 4 mesiace. Hlavné kategórie 6 až 12 mesiacov. Záleží na konkurencii vo vašom sortimente."),
                ("Pracujete so Shoptet a Upgates?", "Áno, Shoptet, Upgates a WooCommerce sú najčastejšie platformy, s ktorými pracujem."),
                ("Koľko hodín potrebuje e-shop mesačne?", "Menší e-shop 20 hodín (240 EUR), stredný 30 hodín (360 EUR), veľký 40 hodín a viac. Spresní to plán po audite."),
            ],
            "related": [
                ("kategorie-seo", "Kategórie e-shopu: ako ich optimalizovať pre Google"),
                ("shoptet-seo", "SEO na Shoptet: čo nastaviť a čo riešiť systémovo"),
            ],
        },
        "cz": {
            "label": "Návod",
            "h1": "SEO pro e-shop: kompletní návod 2026",
            "title": "SEO pro e-shop: kompletní návod 2026 | SEO pro e-shopy",
            "desc": "SEO pro e-shop krok za krokem: kategorie, produkty, technika a feedy. Návod s reálnymi čísly a cenami od 240 EUR měsíčně.",
            "date_display": "17. 9. 2026", "date_iso": "2026-09-17",
            "answer": "SEO pro e-shop je optimalizace kategorií a produktů na dotazy, které zákazníci hledají před nákupem. Struktura kategorií, systémové popisy produktů, řešení filtrů a XML feedy pro Google Shopping. První objednávky z delšího chvostu za 2 až 4 měsíce, cena od 240 EUR měsíčně (12 EUR za hodinu).",
            "sections": """
<h2>Proč e-shop potřebuje jiný SEO než firemní web</h2>
<p>E-shop má tisíce stránek, filtrování a varianty. Google musí rozumět, která URL je správná pro který dotaz. Proto e-shop SEO začíná technikou: duplicitní URL z filtrů, kanonické adresy, strukturovaná data produktů. Každá chyba se násobí počtem stránek.</p>

<h2>Krok 1: Kategorie jako hlavní SEO kanál</h2>
<p>Kategorie jsou stránky, které Google řadí na hlavní dotazy. Každá kategorie potřebuje: text na reálná hledání, správný H1, interní odkazy a filtry bez duplicitních URL. Dotazy ověříte přes Marketing Miner nebo autocomplete.</p>

<h2>Krok 2: Produkty systémově, ne ručně</h2>
<p>Nemůžete optimalizovat 5000 produktů ručně. Nastavte šablony popisů a pravidla: barva + model + použití v názvu, dostupnost ve feedu. Ruční práce jen tam, kde se vyplácí (nejprodávanější produkty).</p>

<h2>Krok 3: Technika a feedy</h2>
<ul>
<li><strong>Filtry</strong>: žádné duplicitní URL, canonical na čistou adresu.</li>
<li><strong>XML feed</strong>: Google Merchant Center se správnými atributy (název, cena, dostupnost, GTIN).</li>
<li><strong>Rychlost</strong>: LCP pod 2,5 s. E-shopy jsou těžké, cache je povinnost.</li>
<li><strong>Schema</strong>: Product + Offer + Review. Google zobrazuje ceny a hodnocení přímo ve výsledcích.</li>
</ul>

<h2>Kolik to stojí</h2>
<p>Menší e-shop: 20 hodin měsíčně = 240 EUR. Střední e-shop: 30 hodin = 360 EUR. Velký e-shop: 40 hodín = 480 EUR. První hodina je bezplatný audit e-shopu.</p>
""",
            "faq": [
                ("Jak dlouho trvá, než e-shop SEO přinese objednávky?", "Delší chvost (produktové fráze s barvou a modelem) 2 až 4 měsíce. Hlavní kategorie 6 až 12 měsíců."),
                ("Pracujete se Shoptet a Upgates?", "Ano, Shoptet, Upgates a WooCommerce jsou nejčastější platformy, se kterými pracuji."),
                ("Kolik hodin potřebuje e-shop měsíčně?", "Menší e-shop 20 hodin (240 EUR), střední 30 hodin (360 EUR), velký 40 hodín a více."),
            ],
            "related": [
                ("kategorie-seo", "Kategorie e-shopu: jak je optimalizovat pro Google"),
                ("shoptet-seo", "SEO na Shoptet: co nastavit a co řešit systémově"),
            ],
        },
    },
    "kategorie-seo": {
        "sk": {
            "label": "Kategórie",
            "h1": "Kategórie e-shopu: ako ich optimalizovať pre Google",
            "title": "SEO pre kategórie e-shopu | SEO pre e-shopy",
            "desc": "Kategórie sú najväčší SEO kanál e-shopu. Ako ich štruktúrovať, písať texty a riešiť filtre. Od 240 EUR mesačne.",
            "date_display": "17. 9. 2026", "date_iso": "2026-09-17",
            "answer": "Kategórie sú najväčší SEO kanál e-shopu: Google ich radí na hlavné dopyty: topánky na behanie, školské tašky. Každá kategória potrebuje text na reálne hľadania, správny H1, interné odkazy a filtre bez duplicitných URL. Kategóriu, ktorá nemá žiadne hľadanie, presmerujte alebo zrušte.",
            "sections": """
<h2>Štruktúra kategórií podľa hľadaní</h2>
<p>Štruktúra kategórií má zodpovedať tomu, čo zákazníci hľadajú, nie internej logike firmy. Dopyty overte cez Marketing Miner (objemy na SK/CZ) alebo autocomplete v Google. Každá hlavná kategória = jeden dopyt s objemom. Podkategórie = dlhší chvost ("dámske topánky na behanie").</p>

<h2>Text kategórie, ktorý Google rád</h2>
<ul>
<li><strong>H1</strong>: presný názov, podľa ktorého zákazníci hľadajú. Nie marketingový slogan.</li>
<li><strong>Úvod (2 až 3 riadky)</strong>: odpoveď na dopyt hneď, nad produktmi.</li>
<li><strong>Nasledujúci text</strong>: pod produktmi, 200 až 400 slov. Pokrýva podotázky (farby, veľkosti, materiály).</li>
<li><strong>Interné odkazy</strong>: z kategórie na súvisiace kategórie a blogové články.</li>
</ul>

<h2>Filte a ich URL</h2>
<p>Filtre (farba, veľkosť, značka) vytvárajú nové URL. Ak Google indexuje každú kombináciu, vznikajú tisíce duplicitných stránok a Google stráca rozsah. Riešenie: canonical na čistú kategóriu alebo noindex na filter URL. Populárne filtre (farba + model) sa dajú vyňať ako stránky s vlastným textom, ak majú hľadania.</p>

<h2>Čo z toho vyplýva pre e-shop</h2>
<p>Kategórie sú práca na mesiace, ale najväčší kanál. Pri mojej spolupráci od 240 EUR mesačne (12 EUR za hodinu) idú kategórie ako prvé: plán podľa hľadaní, texty, filtre a interné odkazy v jednom systéme.</p>
""",
            "faq": [
                ("Koľko textu má mať kategória?", "Úvod 2 až 3 riadky nad produktmi, doplnkový text 200 až 400 slov pod produktmi. Dôležitejšia je relevancia než dĺžka."),
                ("Mám indexovať stránky s filtrami?", "Nie. Filtrované URLCanonicalizujte na čistú kategóriu. Výnimkou sú filtre s vlastnými hľadaniami, tie sa dajú urobiť ako samostatné stránky."),
                ("Píšete texty kategórií za e-shopy?", "Áno, texty píšem na reálne hľadania z dát, nie na generické frázy. Súčasť retainera od 240 EUR mesačne."),
            ],
            "related": [
                ("seo-pre-eshop-navod", "SEO pre e-shop: kompletný návod 2026"),
                ("eshop-seo-cena", "Koľko stojí SEO pre e-shop"),
            ],
        },
        "cz": {
            "label": "Kategorie",
            "h1": "Kategorie e-shopu: jak je optimalizovat pro Google",
            "title": "SEO pro kategorie e-shopu | SEO pro e-shopy",
            "desc": "Kategorie jsou největší SEO kanál e-shopu. Jak je strukturovat, psát texty a řešit filtry. Od 240 EUR měsíčně.",
            "date_display": "17. 9. 2026", "date_iso": "2026-09-17",
            "answer": "Kategorie jsou největší SEO kanál e-shopu: Google je řadí na hlavní dotazy. Každá kategorie potřebuje text na reálná hledání, správný H1, interní odkazy a filtry bez duplicitních URL. Kategorie bez hledání zrušte nebo přesměrujte.",
            "sections": """
<h2>Struktura kategorií podle hledání</h2>
<p>Struktura kategorií má odpovídat tomu, co zákazníci hledají. Dotazy ověříte přes Marketing Miner nebo autocomplete. Každá hlavní kategorie = jeden dotaz s objemem. Podkategorie = dlouhý chvost ("dámské boty na běhání").</p>

<h2>Text kategorie</h2>
<ul>
<li><strong>H1</strong>: přesný název, jak zákazníci hledají. Ne marketingový slogan.</li>
<li><strong>Úvod</strong>: odpověď hned, nad produkty.</li>
<li><strong>Další text</strong>: pod produkty, 200 až 400 slov. Podotázky (barvy, velikosti, použití).</li>
<li><strong>Interní odkazy</strong>: z kategorie na související kategorie a blog.</li>
</ul>

<h2>Filtry a jejich URL</h2>
<p>Filtry vytvářejí nové URL a tisíce duplicitních stránek. Riešení: canonical na čistou kategorii nebo noindex filtrů. Populární filtry (barva + model) s vlastními hledáními jde udělat jako samostatné stránky s textem.</p>

<h2>Kolik to stojí</h2>
<p>Kategorie jsou největší kanál e-shopu. Texty kategorií a řešení filtrů jsou součástí retaineru od 240 EUR měsíčně (12 EUR za hodinu).</p>
""",
            "faq": [
                ("Kolik textu má mít kategorie?", "Úvod 2 až 3 řádky nad produkty, doplnkový text 200 až 400 slov pod produkty. Relevance důležitější než délka."),
                ("Indexovat stránky s filtry?", "Ne, filtrované URL canonicalizujte na čistou kategorii. Výjimkou jsou filtry s vlastními hledáními."),
                ("Píšete texty kategorií?", "Ano, na reálná hledání z dat. Součást retaineru od 240 EUR měsíčně."),
            ],
            "related": [
                ("seo-pre-eshop-navod", "SEO pro e-shop: kompletní návod 2026"),
                ("eshop-seo-cena", "Kolik stojí SEO pro e-shop"),
            ],
        },
    },
    "shoptet-seo": {
        "sk": {
            "label": "Shoptet",
            "h1": "SEO na Shoptet: čo nastaviť a čo riešiť systémovo",
            "title": "SEO na Shoptet: čo nastaviť a čo riešiť | SEO pre e-shopy",
            "desc": "SEO na Shoptet: čo sa dá nastaviť v adminovi, čo vyžaduje zásah do šablóny a ako riešiť filtre a duplicitné URL. Od 240 EUR mesačne.",
            "date_display": "17. 9. 2026", "date_iso": "2026-09-17",
            "answer": "Shoptet má SEO základ dobrý, ale tri veci vyžadujú pozornosť: texty kategórií (v adminovi), duplicitné URL z filtrov (rieši šablóna alebo nastavenie) a XML feed pre Google Merchant Center. Shoptet 5400/mo hľadaní v SK znamená, že veľa e-shopov beží na ňom, konkurencia je tam už tiež.",
            "sections": """
<h2>Čo sa dá nastaviť v Shoptet admine</h2>
<ul>
<li><strong>Meta titulky a popisy</strong>: pri každej kategórii, produkte a stránke. Ručne, nie automaticky.</li>
<li><strong>Texty kategórií</strong>: horný aj dolný text. Píšte na reálne hľadania.</li>
<li><strong>Canonical</strong>: Shoptet to rieši sám pre produkty, filtre treba skontrolovať.</li>
<li><strong>Sitemap</strong>: automaticky, poslať do Search Console.</li>
<li><strong>Shoptet Premium</strong>: advanced SEO nastavenia sú v platenej verzii, vyplatí sa.</li>
</ul>

<h2>Čo na Shoptete býva problém</h2>
<p>Filre vytvárajú tisíce URL, ktoré Google indexuje. Riešenie je v nastaveniach alebo šablóne. Ďalší problém: rovnaké popisy produktov ako od dodávateľa (duplicitný obsah s konkurenciou). Rieši systémová šablóna popisov s vlastnými textami.</p>

<h2>Shoptet vs vlastné riešenie pre SEO</h2>
<p>Shoptet je dobrá voľba pre SEO: rýchly hosting, spravovaná platforma, XML feedy v cene. Obmedzenia: obmedzený prístup ku kódu šablóny a menej priestoru pre technické úpravy. Pre väčšinu e-shopov to nevadí: obsah a kategórie rozhodujú viac než technické detaily.</p>

<h2>Koľko stojí SEO na Shoptete</h2>
<p>Menší Shoptet e-shop: 20 hodín mesačne = 240 EUR. Stredný s obsahom a produktami: 30 hodín = 360 EUR. Veľký so systémovou optimalizáciou: 40 hodín = 480 EUR. Audit Shoptet e-shopu je bezplatný.</p>
""",
            "faq": [
                ("Je Shoptet dobrý pre SEO?", "Áno. Má sitemap, canonical a XML feedy v cene. Limitujúce je menej prístupu ku kódu, ale pre väčšinu e-shopov to nevadí."),
                ("Ako riešiť duplicitné URL z filtrov na Shoptete?", "Nastavením canonical alebo noindex pre filter URL. Čo presne nastaviť, vám ukážem pri audite."),
                ("Optimalizujete aj Shoptet feedy?", "Áno, XML feed pre Google Merchant Center je súčasť technickej práce: správné názvy, atribúty, dostupnosť."),
            ],
            "related": [
                ("seo-pre-eshop-navod", "SEO pre e-shop: kompletný návod 2026"),
                ("kategorie-seo", "Kategórie e-shopu: ako ich optimalizovať pre Google"),
            ],
        },
        "cz": {
            "label": "Shoptet",
            "h1": "SEO na Shoptet: co nastavit a co řešit systémově",
            "title": "SEO na Shoptet: co nastavit a co řešit | SEO pro e-shopy",
            "desc": "SEO na Shoptet: co jde nastavit v adminu, co vyžaduje zásah do šablony a jak řešit filtry a duplicity. Od 240 EUR měsíčně.",
            "date_display": "17. 9. 2026", "date_iso": "2026-09-17",
            "answer": "Shoptet má SEO základy dobré, ale tři věci potřebují pozornost: texty kategorií (v adminu), duplicitní URL z filtrů a XML feed pro Google Merchant Center. Shoptet je nejjednodušší platforma pro běžný e-shop SEO, limitem je přístup ke kódu šablony.",
            "sections": """
<h2>Co jde nastavit v Shoptet adminu</h2>
<ul>
<li><strong>Meta titulky a popisy</strong>: u každé kategorie, produktu i stránky. Ručně, ne automaticky.</li>
<li><strong>Texty kategorií</strong>: horní i dolní. Psát na reálná hledání.</li>
<li><strong>Canonical</strong>: Shoptet to řeší u produktů, filtre zkontrolujte.</li>
<li><strong>Sitemap</strong>: automaticky, poslat do Search Console.</li>
<li><strong>Shoptet Premium</strong>: pokročilé SEO nastavení je v placené verzi.</li>
</ul>

<h2>Co na Shoptetu bývá problém</h2>
<p>Filtry vytvářejí tisíce URL, které Google indexuje. Řešení je v nastavení nebo šabloně. Druhý problém: stejný popis produktu jako od dodavatele, duplicitní s konkurencí. Řeší systém šablon s vlastními texty.</p>

<h2>Shoptet vs vlastní řešení pro SEO</h2>
<p>Shoptet je dobrá volba pro SEO: sitemap, canonical i XML feedy v ceně. Limitem je přístup ke kódu šablony. Pro většinu e-shopů nevadí: kategorie a obsah rozhodují víc než technické detaily.</p>

<h2>Kolik stojí SEO na Shoptetu</h2>
<p>Menší Shoptet e-shop: 20 hodin měsíčně = 240 EUR. Střední s obsahem a produkty: 30 hodin = 360 EUR. Velký se systémovou optimalizací: 40 hodin = 480 EUR. Audit Shoptet e-shopu je bezplatný.</p>
""",
            "faq": [
                ("Je Shoptet dobrý pro SEO?", "Ano. Sitemap, canonical i XML feedy v ceně. Limitem je přístup ke kódu, ale pro většinu e-shopů nevadí."),
                ("Jak řešit duplicitní URL z filtrů?", "Canonical nebo noindex pro URL filtrů. Co přesně nastavit, ukážu při auditu."),
                ("Optimalizujete Shoptet feedy?", "Ano, XML feed pro Merchant Center je součást technické práce."),
            ],
            "related": [
                ("seo-pre-eshop-navod", "SEO pro e-shop: kompletní návod 2026"),
                ("kategorie-seo", "Kategorie e-shopu: jak je optimalizovat pro Google"),
            ],
        },
    },
    "eshop-seo-cena": {
        "sk": {
            "label": "Cena",
            "h1": "Koľko stojí SEO pre e-shop (2026)? Ceny a čo za ne dostanete",
            "title": "Koľko stojí SEO pre e-shop | SEO pre e-shopy",
            "desc": "Cena SEO pre e-shop: 240 až 480 EUR mesačne pri hodinovej sadzbe 12 EUR. Čo je v cene, čo nie a ako spoznať predražený paušál.",
            "date_display": "17. 9. 2026", "date_iso": "2026-09-17",
            "answer": "SEO pre e-shop stojí 240 až 480 EUR mesačne pri transparentnej hodinovej sadzbe 12 EUR: menší e-shop 20 hodín (240 EUR), stredný 30 hodín (360 EUR), veľký so systémovou optimalizáciou 40 hodín (480 EUR). Bezplatný audit e-shopu je prvý krok. Paušály od agentúr bývajú 800 až 2000 EUR mesačne a neviete, čo obsahujú.",
            "sections": """
<h2>Prečo hodinová cena a nie paušál</h2>
<p>Paušál vám povie, koľko platíte, ale nie čo za to. Hodinová sadzba s vykázanou prácou znamená: každý mesiac vidíte, čo sa robilo, koľko hodín a čo to prinieslo. Retainer meníte alebo ukončíte kedykoľvek, bez sankcií.</p>

<h2>Cenové balíčky pre e-shopy</h2>
<ul>
<li><strong>Menší e-shop (do 500 produktov)</strong>: 20 hodín mesačne = 240 EUR. Hlavné kategórie, technické základy, mesačný report.</li>
<li><strong>Stredný e-shop</strong>: 30 hodín = 360 EUR. Plus produkty, XML feedy a 2 blogové články.</li>
<li><strong>Veľký e-shop</strong>: 40 hodín = 480 EUR. Plus systémová optimalizácia produktov, riešenie filtrov a duplicit.</li>
</ul>

<h2>Čo ovplyvňuje cenu</h2>
<p>Rozsah sortimentu (koľko kategórií a produktov), stav techniky (duplicitné URL z filtrov), konkurencia vo vašom segmente a koľko obsahu robíme mesačne. Presný rozsah potvrdím v pláne po bezplatnom audite, žiadne prekvapenia v fakturácii.</p>

<h2>Porovnanie s trhom</h2>
<p>Slovenské a české agentúry ponúkajú e-shop SEO paušály od 500 do 2000 EUR mesačne. Hodinová spolupráca od 240 EUR mesačne je pre väčšinu e-shopov efektívnejšia: platíte za prácu, nie za prémiové kancelárie. Rozdiel nie je v kvalite, ale v tom, ako je cena vykázaná.</p>
""",
            "faq": [
                ("Prečo je vstupný audit bezplatný?", "Lebo rozhodnutie o spolupráci potrebujete podložené číslami. Ak vám čísla nebudú dávať zmysel, nič neplatíte."),
                ("Môžem meniť balíček mesačne?", "Áno, balíčky sú odporúčané rozsahy. Kedykoľvek ich môžete zmeniť bez sankcií."),
                ("Čo keď potrebujem viac hodín v jednom mesiaci?", "Riešime to projektovo: väčšia zmena (migrácia, redesign, nová kategória) ide ako samostatná objednávka mimo retainera."),
            ],
            "related": [
                ("seo-pre-eshop-navod", "SEO pre e-shop: kompletný návod 2026"),
                ("audit-eshopu", "SEO audit e-shopu: čo skontrolovať ako prvé"),
            ],
        },
        "cz": {
            "label": "Cena",
            "h1": "Kolik stojí SEO pro e-shop (2026)?",
            "title": "Kolik stojí SEO pro e-shop | SEO pro e-shopy",
            "desc": "SEO pro e-shop: 240 až 480 EUR měsíčně při hodinové sazbě 12 EUR. Co je v ceně a jak poznat předražený paušál.",
            "date_display": "17. 9. 2026", "date_iso": "2026-09-17",
            "answer": "SEO pro e-shop stojí 240 až 480 EUR měsíčně při transparentní hodinové sazbě 12 EUR: menší e-shop 20 hodin (240 EUR), střední 30 hodin (360 EUR), velký se systémovou optimalizací 40 hodin (480 EUR). Paušály agentur bývají 800 až 2000 EUR měsíčně a nevíte, co obsahují.",
            "sections": """
<h2>Proč hodinová cena a ne paušál</h2>
<p>Paušál vám řekne, kolik platíte, ale ne co za to dostanete. Hodinová sazba s vykázanou prací znamená: každý měsíc vidíte, co se dělalo, kolik hodin a co to přineslo. Balíček měníte nebo ukončíte kdykoliv, bez sankcí.</p>

<h2>Cenové balíčky pro e-shopy</h2>
<ul>
<li><strong>Menší e-shop</strong>: 20 hodin měsíčně = 240 EUR. Hlavní kategorie, technické základy, měsíční report.</li>
<li><strong>Střední e-shop</strong>: 30 hodín = 360 EUR. Plus produkty, XML feedy a 2 články.</li>
<li><strong>Velký e-shop</strong>: 40 hodin = 480 EUR. Plus systémová optimalizace produktů, řešení filtrů a duplicit.</li>
</ul>

<h2>Co ovlivňuje cenu</h2>
<p>Rozsah sortimentu, stav techniky (duplicitní URL z filtrů) a kolik obsahu děláme měsíčně. Přesný rozsah potvrdím v plánu po bezplatném auditu. Žádná překvapení ve fakturaci.</p>

<h2>Porovnání s trhem</h2>
<p>České agentury nabízejí e-shop SEO paušály od 800 do 2000 EUR měsíčně. Hodinová spolupráce od 240 EUR je pro většinu e-shopů efektivnější: platíte za práci, ne za premium kanceláře.</p>
""",
            "faq": [
                ("Proč je vstupní audit bezplatný?", "Protože rozhodnutí o spolupráci potřebujete podložené čísly. Když vám čísla nebudou dávat smysl, nic neplatíte."),
                ("Můžu měnit balíček?", "Ano, balíčky jsou doporučené rozsahy, mění se kdykoliv bez sankcí."),
                ("Co když potřebuji víc hodin v jednom měsíci?", "Řešíme to projektově: větší změna jde jako samostatná objednávka mimo retainer."),
            ],
            "related": [
                ("seo-pre-eshop-navod", "SEO pro e-shop: kompletní návod 2026"),
                ("kategorie-seo", "Kategorie e-shopu: jak je optimalizovat pro Google"),
            ],
        },
    },
}
