import gradio as gr
import json
import src.data_processing as data_processing
import src.prompt_generator as prompt_generator
import src.story_generator as story_generator
import src.image_generator as image_generator

# All available genres (add or edit freely)
GENRES = [
    "Fantasy", "Science Fiction", "Mystery", "Thriller", "Romance", "Horror",
    "Historical Fiction", "Adventure", "Comedy", "Drama", "Western", "Dystopian",
    "Crime", "Mythology", "Slice of Life", "Tragedy"
]

# Build Gradio Interface
with gr.Blocks() as demo:

    gr.Markdown("## :nota: AI Story Generator (Open Source via Hugging Face)")

    with gr.Row():
        story_title = gr.Textbox(label="Story Title", placeholder="Enter your story title...")
        quantity_of_words = gr.Number(label="Quantity of Words", minimum=450, maximum=550, value=500)

    genre = gr.Dropdown(label="Genre", choices=GENRES, value="Fantasy")
    characters = gr.Textbox(label="Characters (comma separated)", placeholder="Alice, Bob, The Dragon...")

    story_data = data_processing.data_processing(story_title, quantity_of_words, genre, characters)
    prompt = prompt_generator.prompt_generator(story_data)
    
    generate_btn = gr.Button("Generate Story")

    with gr.Row():
        story_output = gr.Code(label=":paquete: JSON Parameters", language="json")
    generate_btn.click(fn=story_generator.story_generator, inputs=[story_data, prompt],
                       outputs=story_output)

    # Generar imagen
    story_image = image_generator.image_generator(story_output)
    with gr.Row():
        gr.Image(story_image, label=":art: Generated Story Image")
# Launch app
if __name__ == "__main__":
    demo.launch(share=True, debug=True)