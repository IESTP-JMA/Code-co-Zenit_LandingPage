import reflex as rx
from .componentes.encabezado import encabezado
def index()->rx.Component:
  return rx.box(
    encabezado(),
  )

app=rx.App()
app.add_page(index)