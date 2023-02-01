from PIL import Image

# Открываем исходное изображение
image = Image.open("169169-ty_zasluzhivaesh_vsyacheskogo_schastya-schaste-strah-voda-polety_na_vozdushnom_share-500x.jpg")

# Создаем копию исходного изображения
new_image = image.copy()

# Получаем размеры изображения
width, height = image.size

# Проходимся по каждому пикселю изображения
for x in range(width):
    for y in range(height):
        # Получаем цвет пикселя
        r, g, b = image.getpixel((x, y))
        # Вычисляем среднее значение цвета
        sr = (r + g + b) // 3
        # Устанавливаем новый цвет пикселя
        new_image.putpixel((x, y), (sr, sr, sr))

# Запускаем
new_image.show()

