from django.http import JsonResponse, HttpResponse
from PIL import Image
import os
import io
import base64

def get_items(request):
    return JsonResponse({"items": ["item1", "item2", "item3"]})

def home(request):
    return JsonResponse({"message": "Welcome to the homepage!"})


# outputPath should be something like: "./TestImages/{object}_basicArmor_"
def get_texture_bits(request):
    # Pobieranie parametrów z zapytania GET
    texture_path = request.GET.get("texturePath")
    objects_list = request.GET.getlist("objectsList[]")
    width = int(request.GET.get("width", 64))
    height = int(request.GET.get("height", 80))
    map_width = int(request.GET.get("mapWidth", 4))
    map_height = int(request.GET.get("mapHeight", 4))

    if not texture_path or not objects_list:
        return JsonResponse({"error": "Missing required parameters"}, status=400)

    try:
        # Otwieranie tekstury
        texture = Image.open(texture_path)
        image_list = {}

        list_index = 0
        for u in range(map_width):
            for i in range(map_height):
                if list_index >= len(objects_list):
                    break

                # Tworzenie nowego obrazu z wycinkiem
                image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
                image_pixels = image.load()
                x_offset = width * u
                y_offset = height * i

                for x in range(width):
                    for y in range(height):
                        color = texture.getpixel((x + x_offset, y + y_offset))
                        image_pixels[x, y] = color

                # Kodowanie obrazu jako Base64
                buffered = io.BytesIO()
                image.save(buffered, format="PNG")
                encoded_image = base64.b64encode(buffered.getvalue()).decode("utf-8")

                # Przypisywanie obrazu do obiektu
                image_list[objects_list[list_index]] = f"data:image/png;base64,{encoded_image}"
                list_index += 1

        return JsonResponse({"images": image_list})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
