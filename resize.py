from PIL import Image
import os
import math


main_path = os.path.join(os.getcwd(), 'input_main')

for filename in os.listdir(main_path):
    print("Main: Resizing " + filename)
    file_path = os.path.join(main_path, filename)
    img = Image.open(file_path)
    greater_size = max(img.size[0], img.size[1])
    img = img.resize((math.ceil(img.size[0] / greater_size * 2000), math.ceil(img.size[1]/greater_size * 2000)))
    img.save(os.getcwd() + "/output/resized_" + filename)
    
thumb_path = os.path.join(os.getcwd(), 'input_thumb')

for filename in os.listdir(thumb_path):
    print("Thumb: Resizing " + filename)
    file_path = os.path.join(thumb_path, filename)
    img = Image.open(file_path)
    img = img.resize((200, 200))
    img.save(os.getcwd() + "/output/resized_thumb_" + filename)