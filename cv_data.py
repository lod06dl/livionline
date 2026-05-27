from fasthtml.common import A, Span

THESIS_SPIRAL_URL = "https://spiral.imperial.ac.uk/entities/publication/82a77df1-04bd-42cf-97c1-3d7b7306799a"
NYC_STUDY_URL = "https://www.hraadvisors.com/wp-content/uploads/2024/11/HRA_NYC-Rideshare-Cost-Study_Report_11.04.pdf"

EXPERIENCE = [
    (
        "Applied Scientist – Policy Science",
        "Uber",
        "Jun 2022 – Apr 2026",
        [
            Span(
                "Led a third-party ",
                A(
                    "earnings and cost study",
                    href=NYC_STUDY_URL,
                    cls="link link-primary",
                    target="_blank",
                    rel="noopener noreferrer",
                ),
                " for the NYC pay-standard renegotiation.",
            ),
            "Pioneered an odometer-based analysis quantifying driver incremental mileage in key regulated US markets, strengthening Uber's case for accounting for marginal rather than average driver costs.",
            "Developed and owned Uber's approved methodology for sharing driver-earnings information externally, ensuring global consistency from the CEO's interviews to regulatory data shares.",
            "Prepared C-suite briefs on driver earnings ahead of Davos meetings and interviews.",
        ],
    ),
    (
        "Analytics Team Lead",
        "Beauty Pie",
        "Nov 2020 – May 2022",
        [
            "Joined as the second analytics hire to build the data function from the ground up; scaled and led a team of three.",
            "Designed the analytical data layer (DBT, Snowflake) enabling end-to-end analysis of the consumer funnel, sales, and lifetime value, built from scratch.",
            "Built a demand forecast that reduced stockouts, integrated directly into the NetSuite ERP.",
        ],
    ),
    (
        "Data Lead – Driver Team UK & Ireland",
        "Uber",
        "Jul 2019 – Aug 2020",
        [
            "Informed parts of the UK Government's Self-Employed Income Scheme, the flagship contractor-support package during lockdown.",
            "Scoped financial-support packages and bereavement policies during the pandemic (30k drivers impacted).",
            "Identified flaws in an A/B test of a customer-support programme.",
        ],
    ),
    (
        "Knowledge Engineer – Alexa Information UK",
        "Amazon",
        "Jun 2018 – Jan 2019",
        [
            "Sole UK knowledge engineer designing and maintaining Alexa Q&A features for the British market.",
            'Delivered the first seamless third-party integration into Alexa UK (e.g. "What\'s on BBC One?"), which became the template for scaling Alexa capabilities with minimal internal development.',
        ],
    ),
    (
        "Senior Analyst – Product, Data Science",
        "Criteo",
        "Sep 2016 – Jun 2018",
        [
            "Analysed Criteo's global market penetration; outputs fed directly into investor earnings calls.",
            "Built an internal R package automating analysis and slide production, saving each analyst weeks of work per quarter.",
            "Recognised with two cash prizes: Best Innovative Project (2018) and Super Star Team Award (2017).",
        ],
    ),
    (
        "Programmatic Analyst – Advertising",
        "eBay (contractor)",
        "Nov 2015 – May 2016",
        [
            "Built a performance-tracking database across all display ad networks, covering ~10% of eBay UK revenue.",
            "Managed partnerships with Criteo, Google, Rubicon, OpenX, and AppNexus to ensure data quality and performance.",
        ],
    ),
]

SKILLS = {
    "Technical": [
        "R",
        "Python",
        "SQL",
        "DBT",
        "Snowflake",
        "Vim",
        "AI coding tools (Cursor, Claude, Shell Sage)",
    ],
    "Languages": [
        "🇬🇧 English",
        "🇮🇹 Italian",
        "🇫🇷 French",
        "🇪🇸 Spanish (conversational)",
        "🇷🇺 Russian (basic conversational)",
    ],
}

EDUCATION = [
    (
        "PhD – Wave Mechanics",
        "Imperial College London",
        "2010 – 2017",
        [
            Span(
                "Thesis: ",
                A(
                    '"Extreme waves in intermediate and shallow water depths"',
                    href=THESIS_SPIRAL_URL,
                    cls="link link-primary",
                    target="_blank",
                    rel="noopener noreferrer",
                ),
                ", supervised by Prof. Chris Swan. Published in the Journal of Coastal Engineering.",
            ),
            "Selected for McKinsey's Insight Program (top 60 UK PhDs).",
        ],
    ),
    (
        "MEng Civil Engineering – First Class Honours",
        "Imperial College London",
        "2006 – 2010",
        [
            "Exchange year at École Nationale des Ponts et Chaussées, Paris (First Class Honours).",
        ],
    ),
]

AWARDS = [
    "Criteo Best Innovative Project Award, 2018 – UTM data to inform account managers on clients' marketing mix.",
    "Criteo Super Star Team Award, 2017 – Awarded to the Accelerate team for growth and impact.",
    "McKinsey & Co Insight Program, 2013 – Selected among 60 top UK PhD candidates for a workshop in Austria.",
    "Publication in Journal of Coastal Engineering, 2013 – Large waves in intermediate and shallow water depths.",
]

INTERESTS = (
    "Kitesurfing · Marathons (four run in California) · Sailing (qualified instructor)"
)
