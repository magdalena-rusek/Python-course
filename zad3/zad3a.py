def usunSlowa(words, path):
 for word in words:
  file = open(path, "rt") 
  data = file.read()
  data = data.replace(word, '')
  file.close()
  file = open(path, "wt") 
  file.write(data)
  file.close()

words = ['partly', 'is', 'parts', 'of']
path1 = "files/3sat.txt"
path2 = "files/7TP.txt"
path3 = "files/ABC2.txt"

usunSlowa(words, path1)
usunSlowa(words, path2)
usunSlowa(words, path3)
