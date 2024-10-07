
import xml.dom.minidom
def main():
    doc=xml.dom.minidom.parse("Chuong_2/sample.xml")
    print(doc.nodeName)
    print(doc.firstChild.tagName)
#---------------
    staff = doc.getElementsByTagName("staff")
    print("%d staff:" % staff.length) 
    for information in staff: 
        name=information.getElementsByTagName('name')
        salary=information.getElementsByTagName('salary')
        print("Staff id =",information.getAttribute("id"))
        for i in name:
            print(i.firstChild.data)
        for i in salary:
            print(i.firstChild.data)
if __name__=="__main__": 
   main()