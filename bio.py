from fasthtml.common import *
from cv_data import EXPERIENCE, SKILLS, EDUCATION, AWARDS, INTERESTS
from nav import with_nav

def Job(title, co, period, bullets):
    """Each bullet may be a str or a FastHTML fragment (e.g. Span + A for inline links)."""
    return Div(
        Div(
            H3(title, cls='font-semibold text-base'),
            Span(co, cls='text-sm opacity-60'),
            Span(' · ' + period, cls='text-xs opacity-40 ml-1'),
            cls='mb-2'
        ),
        Ul(*[Li(b, cls='text-sm opacity-75') for b in bullets], cls='list-disc ml-4 space-y-1'),
        cls='pl-4 border-l-2 border-primary mb-6'
    )

def Badges(*items):
    return Div(*[Span(s, cls='badge badge-outline badge-sm') for s in items], cls='flex flex-wrap gap-2')

def Section(title, *content):
    return Div(
        P(title, cls='text-xs font-bold uppercase tracking-widest opacity-40 mb-4'),
        *content,
        cls='mb-10'
    )


def page():
    experience = Section("Experience", *[Job(*e) for e in EXPERIENCE])
    skills     = Section("Skills",
                     *[Div(P(label, cls='text-sm font-semibold mb-2'), Badges(*items), cls='mb-4')
                       for label, items in SKILLS.items()])
    education  = Section("Education",  *[Job(*e) for e in EDUCATION])
    awards     = Section("Awards & Publications",
                     Ul(*[Li(a, cls='text-sm opacity-75') for a in AWARDS], cls='list-disc ml-4 space-y-2'))
    interests  = Section("Interests", P(INTERESTS, cls='text-sm opacity-75'))

    return with_nav(
        Div(
            H1("Livio de Lutio", cls="text-3xl font-bold"),
            P("Data Scientist", cls="opacity-50 mt-1 mb-10"),
            experience,
            skills,
            education,
            awards,
            interests,
            cls="max-w-[760px] mx-auto px-6 py-12 flex-1 w-full",
        )
    )

