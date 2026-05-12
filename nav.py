from fasthtml.common import *

def site_nav():
    """Single link row — avoids duplicate Home/CV when Pico or CSS order breaks lg:/hidden utilities."""
    links = Ul(
        Li(A("Home", href="/")),
        Li(A("CV", href="/cv")),
        cls="menu menu-horizontal px-1",
    )
    return Div(
        Div(
            Div(
                A(
                    "Livio de Lutio",
                    href="/",
                    cls="btn btn-ghost text-lg sm:text-xl font-semibold tracking-tight",
                ),
                cls="navbar-start",
            ),
            Div(links, cls="navbar-end"),
            cls="navbar bg-base-100 w-full flex-wrap gap-y-2 border-b border-base-200 shadow-sm",
        ),
        cls="sticky top-0 z-50 w-full",
    )


def with_nav(main):
    """Stack the sticky navbar above page content (use from home/bio `page`)."""
    return Div(site_nav(), main, cls="min-h-screen flex flex-col")
