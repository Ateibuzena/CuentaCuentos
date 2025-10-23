# 📚 CuentaCuentos – Order Processing

**CuentaCuentos** es un pipeline de generación y validación de relatos breves mediante IA.  
El sistema recibe parámetros (nombre del relato, tema, tamaño,...) y genera automáticamente varias versiones de un texto, las valida, selecciona la mejor y crea una imagen representativa.

---

## 🧩 Flujo de trabajo

1. **Receive Input (JSON)** → se definen parámetros: nombre, tamaño, tema.  
2. **Processing Data** → validación de parámetros y limpieza.  
3. **Create Prompt** → construcción del prompt para generación de textos.  
4. **Generate 5 Texts** → se generan 5 versiones del relato.  
5. **Validate Form** → control de formato (longitud, estructura).  
6. **Validate Content** → detección de coherencia y tono.  
7. **Best Selection** → elección del relato más coherente.  
8. **Generate Image** → creación de imagen basada en el relato.  
9. **Export and Save** → exportación del resultado final.

---

## 🛠️ Tecnologías sugeridas
- **Python 3.10+**
- `openai` o `transformers` (para generación de texto)
- `pydantic` (para validación)
- `Pillow` o `stable-diffusion` API (para imágenes)
- `pytest` (para testing)
- `json` / `yaml` (para entrada y salida de datos)

---

## 🚀 Ejecución
```bash
pip install -r requirements.txt
python src/main.py --input params.json
```
---

## Estructura
CuentaCuentos/
│
├── src/
│   ├── main.py
│   ├── prompt_generator.py
│   ├── text_validator.py
│   ├── image_generator.py
│   └── utils/
│       └── data_processing.py
│
├── tests/
│   ├── test_prompt_generator.py
│   ├── test_text_validator.py
│   └── ...
│
├── assets/
│   └── diagrams/
│       └── Order_Processing.png
│
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE

# 📈 Próximos pasos

Añadir interfaz web (Flask/FastAPI)

Integrar base de datos para almacenar relatos

Crear panel de selección de resultados


---

## 🧠 Este repositorio muestra:
- Un flujo **bien modularizado**.  
- Separación clara entre procesamiento, validación, y generación.  
- Uso de **nombres semánticos y estructurados**.  
- Un README explicativo que documenta tu razonamiento.  
- Posible expansión a IA o automatización (encaja perfecto con el enfoque del reto).

---

## 🧾 Para completarlo

| Elemento | Qué mostrar | Por qué suma puntos |
|-----------|--------------|--------------------|
| `requirements.txt` | Lista exacta de dependencias 
| `README.md` | Explicación clara, pipeline, y ejecución 
| `assets/` | Incluye el diagrama que has subido 
| `tests/` | Unit tests simples (por ejemplo, validar longitud de texto) 
| `main.py` | Pipeline central que llame a las demás funciones
