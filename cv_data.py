from fasthtml.common import A, Span

THESIS_SPIRAL_URL = "https://spiral.imperial.ac.uk/entities/publication/82a77df1-04bd-42cf-97c1-3d7b7306799a"

EXPERIENCE = [
    ("Applied Scientist – Policy Science", "Uber", "Jun 2022 – Apr 2026", [
        "Responsible for external-facing earnings claims (governments, investors, press).",
        "Commissioned external report on rideshare economics in NYC, leading to 50M+ in yearly savings in TLC pay standard negotiations.",
        "Introduced novel odometer analysis to support marginal cost arguments in regulatory proceedings.",
    ]),
    ("Analytics Team Lead", "Beauty Pie", "Nov 2020 – May 2022", [
        "Designed analytical data pipelines (DBT, Snowflake).",
        "Built automated product demand forecast with dashboards integrated into the ERP.",
        "Designed & analysed website A/B tests.",
    ]),
    ("Data Lead – Driver Team UK & Ireland", "Uber", "Jul 2019 – Aug 2020", [
        "Delivered analyses to Government on contractor support during lockdown, informing the UK Self-Employed Income Scheme.",
        "Scoped & launched Uber Medics for the NHS – up to 40% of trips during lockdown.",
        "Identified a flawed A/B test in a customer support programme, which had mistakenly attributed 1.3M$ benefit",
    ]),
    ("Knowledge Engineer – Alexa Information UK", "Amazon", "Jun 2018 – Jan 2019", [
        'Designed and maintained Alexa Q&A capabilities for over 15 milion customers (e.g. "What\'s on BBC One?").',
        "First seamless third-party app integration into core Alexa, enabling scalable expansion of Alexa's abilities.",
    ]),
    ("Senior Analyst – Product, Data Science", "Criteo", "Sep 2016 – Jun 2018", [
        "Market penetration analysis and opportunity sizing for investor and public communication.",
        "Built internal R package standardising frequent data pulls; ML script for automated sales lead generation.",
        "Trained and mentored all new analysts.",
    ]),
    ("Programmatic Analyst – Advertising", "eBay / Parasol Group", "Nov 2015 – May 2016", [
        "Owned UK advertising reporting and designed a global performance tracking database.",
        "Managed relationships with principal partners (Criteo, Google, Rubicon, OpenX, AppNexus).",
    ]),
]

SKILLS = {
    "Languages": ["🇬🇧 English", "🇮🇹 Italian", "🇫🇷 French", "🇪🇸 Spanish (working)", "🇷🇺 Russian (basic)",],
    "Technical":  [ "R", "Python","SQL", "DBT"],
}

EDUCATION = [
    ("PhD – Wave Mechanics", "Imperial College London", "2010 – 2017", [
        "Fully funded under Prof. Chris Swan.",
        Span(
            "Thesis: ",
            A(
                '"Extreme waves in intermediate and shallow water depths"',
                href=THESIS_SPIRAL_URL,
                cls="link link-primary",
                target="_blank",
                rel="noopener noreferrer",
            ),
            ".",
        ),
        "Key areas of research: short-term statistics, wave kinematics, wave breaking.",
    ]),
    ("Master of Engineering | Civil Engineering, ", "École Nationale des Ponts et Chaussées (exchange)", "2009 – 2010", [
    ]),
    ("Master of Engineering | Civil Engineering, first class honours", "Imperial College London", "2006 – 2010", [
    ]),
]

AWARDS = [
    "Criteo Best Innovative Project Award, 2018 – UTM data to inform account managers on clients' marketing mix.",
    "Criteo Super Star Team Award, 2017 – Awarded to the Accelerate team for growth and impact.",
    "McKinsey & Co Insight Program, 2013 – Selected among 60 top UK PhD candidates for a workshop in Austria.",
    "Publication in Journal of Coastal Engineering, 2013 – Large waves in intermediate and shallow water depths.",
]

INTERESTS = "Kite surfing · Marathon (4× California) · Sailing (qualified instructor)"
