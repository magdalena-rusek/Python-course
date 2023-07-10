import xml.sax

class BookHandler(xml.sax.ContentHandler):
 def __init__(self):
  self.CurrentData = ""
  self.title = ""
  self.author = ""
  self.year = ""
  self.price = ""

 def startElement(self, tag, attribute):
  self.CurrentData = tag
  if tag == "book":
   print("-----BOOK-----")
   print("Category: {}".format(attribute['category']))

 def endElement(self, tag):
  if self.CurrentData == "title":
   print("Title: {}".format(self.title))
  elif self.CurrentData == "author":
   print("Author: {}".format(self.author))
  elif self.CurrentData == "year":
   print("Year: {}".format(self.year))
  elif self.CurrentData == "price":
   print("Price: {}".format(self.price))
  self.CurrentData = ""

 def characters(self, content):
  if self.CurrentData == "title":
   self.title = content
  elif self.CurrentData == "author":
   self.author = content
  elif self.CurrentData == "year":
   self.year = content
  elif self.CurrentData == "price":
   self.price = content
 
parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces, 0)

Handler = BookHandler()
parser.setContentHandler(Handler)

parser.parse("books.xml")

# no modifications because sax parser is read-only
