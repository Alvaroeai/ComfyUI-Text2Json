import json

class TextToJsonNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {
                    "multiline": True,  # Permitir entrada JSON de varias líneas si es necesario
                    "default": '{"name": "Hotel Comfy", "location": "New York"}'
                }),
            }
        }

    RETURN_TYPES = ("JSON",)  # Define el tipo de salida como JSON
    FUNCTION = "process"      # Nombre del método de entrada
    CATEGORY = "conversion"    # Categoría en la interfaz de usuario
    OUTPUT_NODE = False        # Indica que este nodo no es un nodo de salida

    def process(self, text):
        try:
            # Convertir el string en JSON
            json_data = json.loads(text)
            return (json_data,)  # Devolver el JSON como tupla
        except json.JSONDecodeError:
            # En caso de error, devolver un mensaje de error
            return ({"error": "Invalid JSON string"},)

# Registrar el nodo en ComfyUI
NODE_CLASS_MAPPINGS = {
    "TextToJson": TextToJsonNode
}
