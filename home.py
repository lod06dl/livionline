from fasthtml.common import *
from nav import with_nav

l = [ 
        ["linkedin-svgrepo-com.svg", "https://www.linkedin.com/in/livio-de-lutio-phd-2706495b/"],
        ["github.svg", "https://github.com/lod06dl"],
        ["mail.svg", "mailto:livio@livionline.me"],
    ]
def Ikn(src, href, *, img_cls="h-9 w-9", **img_kw):
    """One list item: linked icon image."""
    return Li(A(Img(src=src, cls=img_cls, **img_kw), href=href))


def page():
    ava_livio = Div(
        Div(
            Div( Img(src='Livio_cartoon.png'), cls='w-72 rounded-full'), cls='avatar'
        )
        , cls='flex justify-center items-center'
    )
    social_links = Ul(
        *[Ikn(src, href) for src, href in l],
        cls="menu menu-horizontal bg-base-100 rounded-box px-0.5 py-0.5",
    )
   
    about_me = P(
            """Hi, I am Livio! A reformed civil engineer, now a Data Scientist. For the past 10 years, 
            I have been working in tech, at the centre of the public conversation: Uber, Amazon, Criteo, and eBay. 
            I've left San Francisco and am newly based in Belgium, looking for smart and fun people to build with. 
            Reach out for tech conversations, share secret kitesurfing spots, or your favourite cooking recipe. 
            If you're in Belgium, let's grab coffee!""" , cls="leading-relaxed")
    
    return with_nav(
        Div(
            ava_livio,
            Titled(
                "Livio de Lutio",
                P(
                    "Civil engineer turned data scientist. The PhD gathers dust; the curiosity doesn't.",
                    cls="opacity-70",
                ),
                cls="text-center w-full",
            ),
            social_links,
            about_me,
            cls="hero flex flex-col items-center justify-center flex-1 gap-2 max-w-[900px] mx-auto w-full px-4",
        )
    )
