from PIL import Image

img1 = Image.open(r"/home/mr/Pulpit/python/zad2/img/image1.jpg")
img2 = Image.open(r"/home/mr/Pulpit/python/zad2/img/image2.jpg")
img3 = Image.open(r"/home/mr/Pulpit/python/zad2/img/image3.jpg")
img4 = Image.open(r"/home/mr/Pulpit/python/zad2/img/image4.jpg")

img1 = img1.save(r"/home/mr/Pulpit/python/zad2/img/img1.png")
img2 = img2.save(r"/home/mr/Pulpit/python/zad2/img/img2.png")
img3 = img3.save(r"/home/mr/Pulpit/python/zad2/img/img3.png")
img4 = img4.save(r"/home/mr/Pulpit/python/zad2/img/img4.png")


