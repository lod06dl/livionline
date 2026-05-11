import home
from fasthtml.common import *
import fasthtml.components as fc

daisy_hdrs = (
    Link(href='https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap', rel='stylesheet'),
    Link(href='https://cdn.jsdelivr.net/npm/daisyui@5', rel='stylesheet', type='text/css'),
    Script(src='https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4'),
    Link(href='https://cdn.jsdelivr.net/npm/daisyui@5/themes.css', rel='stylesheet', type='text/css'),
    Style('* { font-family: "Inter", sans-serif; }'),
)

app,rt = fast_app(hdrs=daisy_hdrs, static_path='static', title='Livio de Lutio', pico=True)

app.get('/')(home.page)
# app.get('/cv')(cv.page)

serve()

