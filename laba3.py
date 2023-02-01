from PIL import Image

def blur_image(image_path):
    original = Image.open(image_path)
    blurred = original.copy()

    width, height = original.size
    for x in range(width):
        for y in range(height):
            sosed = []
            #Вычисляем среднее значение пикселя
            for dx in [-2, 0, 2]:
                for dy in [-2, 0, 2]:
                    x_coord = x + dx
                    y_coord = y + dy
                    if x_coord >= 0 and x_coord < width and y_coord >= 0 and y_coord < height:
                        sosed.append(original.getpixel((x_coord, y_coord)))
            red_sum = 0
            green_sum = 0
            blue_sum = 0
            #Присваиваем среднее значение пикселей пикселю
            for red, green, blue in sosed:
                red_sum += red
                green_sum += green
                blue_sum += blue
            num_neighbors = len(sosed)
            blurred.putpixel((x, y), (red_sum // num_neighbors, green_sum // num_neighbors, blue_sum // num_neighbors))
    return blurred

new_image = blur_image("169169-ty_zasluzhivaesh_vsyacheskogo_schastya-schaste-strah-voda-polety_na_vozdushnom_share-500x.jpg")
new_image.show()
