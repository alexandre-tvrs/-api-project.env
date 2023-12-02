from starlette.responses import HTMLResponse


def get_redoc_html(
    *,
    openapi_url: str,
    title: str = "Project.env",
    redoc_favicon_url: str = "https://fastapi.tiangolo.com/img/favicon.png",
    with_google_fonts: bool = True,
) -> HTMLResponse:
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <title>{title}</title>
    <!-- needed for adaptive design -->
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    """
    if with_google_fonts:
        html += """
    <link href="https://fonts.googleapis.com/css?family=Montserrat:300,400,700|Roboto:300,400,700" rel="stylesheet">
    """
    html += f"""
        <link rel="shortcut icon" href="{redoc_favicon_url}">
        <!--
        ReDoc doesn't change outer page styles
        -->
        <style>
          body {{
            margin: 0;
            padding: 0;
          }}
        </style>
        </head>
        <body>
        <div id="redoc_container"></div>
        <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/redoc-try-it-out/dist/try-it-out.min.js"></script>
        <script>
            RedocTryItOut.init(
                "http://127.0.0.1:8000/openapi.json",
                {{ title: '{title}' }}, 
                document.getElementById("redoc_container"
                )
            )
        </script>
        </script>
      </body>
        </html>
        """
    return HTMLResponse(html)