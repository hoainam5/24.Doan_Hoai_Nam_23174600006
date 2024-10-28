import xml.dom.minidom

def main():
    doc=xml.dom.minidom.parse("Chuong_2/sample.xml")
    print(doc.nodeName)
    print(doc.firstChild.tagName)
    print(doc.documentElement.nodeName)
if __name__=="__main__":
    main()
