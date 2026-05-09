from fasthtml.common import *
import fasthtml.components as fc

daisy_hdrs = (
    Link(href='https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap', rel='stylesheet'),
    Link(href='https://cdn.jsdelivr.net/npm/daisyui@5', rel='stylesheet', type='text/css'),
    Script(src='https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4'),
    Link(href='https://cdn.jsdelivr.net/npm/daisyui@5/themes.css', rel='stylesheet', type='text/css'),
    Style('* { font-family: "Inter", sans-serif; }'),
)


def Ikn(*arg, cls='h-9 w-9', **kwargs): return  Img(*arg, cls=cls, **kwargs)

app,rt = fast_app(hdrs=daisy_hdrs, static_path='/home/ubuntu/livionline/static', title='Livio de Lutio', pico=True)

@rt
def index(): # Special name for "/"
    ava_livio = Div(
        Div(
            Div( Img(src='zoo2.jpg'), cls='w-72 rounded-full'), cls='avatar'
        )
        , cls='flex justify-center items-center'
    )
    dock_lnks = Ul(
        Li(A(Ikn(src='linkedin-svgrepo-com.svg'), href='https://www.linkedin.com/in/livio-de-lutio-phd-2706495b/')),
        Li(A(Ikn(src='github.svg') , href='https://github.com/lod06dl')),
        Li(A(Ikn(src='mail.svg') , href='mailto:livio@livionline.me')),
        cls='menu menu-horizontal bg-base-300 rounded-box px-0.5 py-0.5'
    )
   
    about_me = P(
            """Hi, I am Livio! A reformed civil engineer, now a Data Scientist. For the past 10 years, 
            I have been working in tech, at the centre of the public conversation: Uber, Amazon, Criteo, and eBay. 
            I've left San Francisco and am newly based in Belgium, looking for smart and fun people to build with. 
            Reach out for tech conversations, share secret kitesurfing spots, or your favourite cooking recipe. 
            If you're in Belgium, let's grab coffee!""" , cls="leading-relaxed")
    
    return Div(
            ava_livio,
            H1('Livio de Lutio'),
            P("Civil engineer turned data scientist. The PhD gathers dust; the curiosity doesn't."),
            dock_lnks, 
            about_me,
            cls='hero flex flex-col items-center justify-center min-h-screen gap-2 max-w-[900px] mx-auto'
            )

serve()
