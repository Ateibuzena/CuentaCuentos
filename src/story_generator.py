def story_generator_all_models(story_data, prompt):
    all_outputs = []

    for model_name in text_gen_models:
        try:
            client = InferenceClient(model=model_name)

            # Generar la historia
            response = client.text_generation(prompt, max_new_tokens=story_data['quantity_of_words'])
            story_text = response.generated_text

            # Crear JSON
            output = {
                "model": model_name,
                "title": story_data['title'],
                "word_count": story_data['quantity_of_words'],
                "genre": story_data['genre'],
                "characters": story_data['characters'],
                "story": story_text
            }

            all_outputs.append(output)

        except Exception as e:
            print(f"Error con el modelo {model_name}: {e}")
            # Guardar un JSON de error para este modelo
            all_outputs.append({
                "model": model_name,
                "error": str(e)
            })

    return all_outputs