from PIL import Image
image_path='1.jpg'
image=Image.open(image_path)
info=image.info
print(info)

info['meta']='example meta data'
new_image_path='new_image.jpg'
image.save(new_image_path,format='JPEG',**info)