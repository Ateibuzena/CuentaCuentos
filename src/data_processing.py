import json

def data_processing(story_title, quantity_of_words, genre, characters):

    """

    Procesa los datos de entrada para estructurarlos en un formato JSON adecuado para la generación de imágenes.

    """
    
    story_data = {
        "title": story_title,
        "quantity_of_words": quantity_of_words,
        "genre": genre,
        "characters": [char.strip() for char in characters.split(",") if char.strip()]
    }
    return json.dumps(story_data, indent=4)