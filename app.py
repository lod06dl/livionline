from fasthtml.common import *

daisy_hdrs = (
    Link(href='https://cdn.jsdelivr.net/npm/daisyui@5', rel='stylesheet', type='text/css'),
    Script(src='https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4'),
    Link(href='https://cdn.jsdelivr.net/npm/daisyui@5/themes.css', rel='stylesheet', type='text/css')
)

app,rt = fast_app(hdrs=daisy_hdrs, static_path='/home/ubuntu/livionline/static')

@rt
def photo():
    return Div(
        Div(
            Img(src='zoo2.jpg'),
            cls='w-72 rounded-full'
        ),
        cls='avatar'
    )

serve()
