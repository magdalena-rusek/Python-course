def zamienSlowa(words, path):
 for key, value in words.items():
  file = open(path, "rt") 
  data = file.read()
  data = data.replace(key, value)
  file.close()
  file = open(path, "wt") 
  file.write(data)
  file.close()

words = {'partly':'important', 'is':'plays', 'parts':'pieces', 'of':'from'}
path1 = "files/3sat.txt"
path2 = "files/7TP.txt"
path3 = "files/ABC2.txt"

zamienSlowa(words, path1)
zamienSlowa(words, path2)
zamienSlowa(words, path3)
