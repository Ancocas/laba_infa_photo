from PIL import Image

def flip_image(image):
    width, height = image.size
    flipped_image = Image.new("RGB", (width, height))
    for x in range(width):
        for y in range(height):
            original_pixel = image.getpixel((x, y))
            flipped_image.putpixel((width-x-1, y), original_pixel)
    return flipped_image

original = Image.open("169169-ty_zasluzhivaesh_vsyacheskogo_schastya-schaste-strah-voda-polety_na_vozdushnom_share-500x.jpg")
flipped = flip_image(original.copy())
flipped.show()

