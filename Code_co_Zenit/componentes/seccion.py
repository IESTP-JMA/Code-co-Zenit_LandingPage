import reflex as rx

def seccion() -> rx.Component:
  return rx.vstack(
      rx.heading(
          rx.text("La única aplicación que necesitas para tener una mejor salud mental",size="8",color=rx.color("blue", 10),text_shadow="1px 1px 1px white")
      ),
      rx.container(
          rx.hstack(
              rx.text("Con esta aplicación podrás interactuar con profesionales expertos en salud mental, que te ayudarán a concientizar tu salud y bienestar mental.",
              #text_shadow="1px 1px 1px black",
              margin_top="8em",
              weight="bold",
              size="5"
              ),
              rx.image(src="https://static.vecteezy.com/system/resources/thumbnails/010/873/204/small_2x/3d-man-is-experiencing-stress-because-of-work-illustration-png.png",
              width="350px",
              margin_top="1em",
              align_items="center"
              ),
              spacing="2em"
          ),
                rx.link(
        rx.button("REGÍSTRATE", margin_top="1em",size="4"),
        href="https://forms.gle/6xSiua2Y2SkrXDG98",
        is_external=True),
      ),
      padding_top="2em",
      align="center",
      text_align="center",
      height="676px",
      background=rx.color("slate",5),
      #background="linear-gradient(175deg, #a1f6b2, #a5f2d0)"
  )