from xml.dom import minidom

domtree = minidom.parse("books.xml")
bookstore = domtree.documentElement

books = bookstore.getElementsByTagName('book')

for book in books:
 print("-------BOOK-------")
 if book.hasAttribute('category'):
  print("Category: {}".format(book.getAttribute('category')))
 print("Title: {}".format(book.getElementsByTagName('title')[0].childNodes[0].data))
 print("Author: {}".format(book.getElementsByTagName('author')[0].childNodes[0].data))
 print("Year: {}".format(book.getElementsByTagName('year')[0].childNodes[0].data))
 print("Price: {}".format(book.getElementsByTagName('price')[0].childNodes[0].data))

books[2].getElementsByTagName('price')[0].childNodes[0].nodeValue = "25.00"
domtree.writexml(open('books_2.xml', 'w'))
