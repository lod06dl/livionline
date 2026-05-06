# Static Image Serving in FastHTML — What Went Wrong

## The Problem

Trying to render an image with:

```python
app = FastHTML(static_path='static')

@rt
def photo():
    return Img(src='/sleeping_cat.jpg')
```

resulted in the image returning a **404**, even though the file existed at `static/sleeping_cat.jpg`.

## Root Cause

`static_path` is **not** a constructor parameter for `FastHTML()`. The class signature does not accept it, so it silently falls into `**bodykw` — a catch-all that gets forwarded as HTML attributes on the `<body>` tag. The rendered HTML revealed this:

```html
<body static-path=static>
```

No static file route was ever registered. The app had no idea how to serve `.jpg` files.

## Solutions

### Option 1 — `static_route_exts` (current working solution)

Call `app.static_route_exts()` explicitly after creating the app:

```python
app = FastHTML()
app.static_route_exts(static_path='/home/ubuntu/livionline/static')
rt = app.route

@rt
def photo():
    return Img(src='/sleeping_cat.jpg')

serve()
```

Use an absolute path to avoid ambiguity with the working directory. This registers the route `/{fname:path}.{ext:static}` which matches all standard static extensions (jpg, png, css, js, etc.).

### Option 2 — Manual route with `FileResponse`

```python
@rt(/{fname:path}.{ext:static}, methods=['GET'])
def static_handler(fname: str, ext: str):
    return FileResponse(f'static/{fname}.{ext}')
```

More explicit, useful if you need custom logic per file type.

## Where the Docs Could Have Helped

The FastHTML API reference documents both methods:

- `static_route_exts(self, prefix='/', static_path='.', exts='static')` — serves all standard static extensions from a directory
- `static_route(self, ext='', prefix='/', static_path='.')` — serves a single extension

These are listed at <https://fastht.ml/docs/llms-ctx.txt> under **fasthtml.core**.
