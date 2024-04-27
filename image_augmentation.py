from PIL import Image
import os


directory = 'dataset_3'




for sub in os.listdir(directory):

    subfoler = os.path.join(directory,sub)    
    for files in os.listdir(subfoler):
        a = files.split('.')
        file = os.path.join(subfoler,files)
        img = Image.open(file)
        rotate_img = img.rotate(35)
        transpose_img = img.transpose(Image.TRANSPOSE)
        rotate_img = rotate_img.convert('RGB')
        transpose_img = transpose_img.convert('RGB')
        rotate_img = rotate_img.save(f'{subfoler}\\{a[0]}_rotate.jpg')
        transpose_img = transpose_img.save(f'{subfoler}\\{a[0]}_transpose.jpg')

        



# img = Image.open("D:\\digit_Dataset\\data_2.0\\train\\Camel\\1_jpg.rf.c5726f0606a4a28b68244699694f51b9.jpg")




# rotate_img = img.transpose(Image.TRANSPOSE)

# img.show()
# rotate_img.show()
