from fasthtml.common import *
import fasthtml.components as fc

daisy_hdrs = (
    Link(href='https://cdn.jsdelivr.net/npm/daisyui@5', rel='stylesheet', type='text/css'),
    Script(src='https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4'),
    Link(href='https://cdn.jsdelivr.net/npm/daisyui@5/themes.css', rel='stylesheet', type='text/css')
)


def Ikn(*arg, cls='h-9 w-9', **kwargs): return  Img(*arg, cls=cls, **kwargs)

app,rt = fast_app(hdrs=daisy_hdrs, static_path='/home/ubuntu/livionline/static', live=True)

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
        Li(A(Ikn(src='mail.svg') , href='mailto:liviodeluti.o@gmail.com')),
        cls='menu menu-horizontal bg-base-300 rounded-box'
    )
    
    return Div(ava_livio, H1('Livio de Lutio'),dock_lnks, cls='flex flex-col items-center justify-center min-h-screen gap-2') 

serve()
