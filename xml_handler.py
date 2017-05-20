from bs4 import BeautifulSoup

from file_handler.file_handler import FileHandler


class XMLHandler(FileHandler):
    def preview(self):

        print self.get_xml().prettify()

    def get_xml(self):
        return BeautifulSoup(self.get(), 'html.parser')

    def extract(self, element):
        for row in self.get_xml().find_all(str(element)):
            for child in row.children:
                print '{0}: {1}'.format(child.name, child.string)
            print ''

if __name__ == '__main__':
    xml = XMLHandler('/home/alissa/PycharmProjects/xml_handler/xml-files/nyc-social-media.xml')
    xml.extract('row')
