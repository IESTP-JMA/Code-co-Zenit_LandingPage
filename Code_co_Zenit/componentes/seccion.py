import reflex as rx
def seccion()->rx.Component:
  return rx.vstack(
      rx.heading(
        rx.text(" La única aplicacion que necesitas ",size="7",color=rx.color("blue",10)),
        rx.text("para tener una mejor salud mental",size="7",color=rx.color("blue",10))),

      rx.container(
        rx.text("Con esta aplicacion podras interactuar con profesionaes ",
        rx.text("expertos en salud mental, que te ayudara a concientizar tu salud mental")),
        rx.link(rx.button("REGISTRATE",margin_top="4em"),href="https://forms.gle/6xSiua2Y2SkrXDG98",is_external=True),
        margin_top="1em"
      ),
      padding_top="8em",
      align="center",
      text_align="center",
      #background="linear-gradient(0deg, rgba(14,12,135,1) 0%, rgba(0,0,0,1) 100%)",
      height="800px"
    )