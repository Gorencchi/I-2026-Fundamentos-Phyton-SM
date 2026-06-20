import gradio
demo = gradio.Blocks()
with demo:
    gradio.Markdown("Registro")
    gradio.Textbox("Nombre: ")
    gradio.Button("Enviar")
    
demo.launch()