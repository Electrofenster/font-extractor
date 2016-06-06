import urllib
from bs4 import BeautifulSoup

class IonIconsUnicodeResolver:
    html = False
    unicodes = {}

    def __init__(self, url):
        self.getHtmlFromUrl(url)
        self.saveAsSass()

    def getHtmlFromUrl(self, url):
        try:
            htmlfile = urllib.urlopen(url)
            response = htmlfile.read()
            self.html = response
        except:
            return False

        self.getUnicodeFromHtml()

    def getUnicodeFromHtml(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        divs = soup.findAll('div', { 'class': 'icon-row' })

        for div in divs:
            icon = div.find('input', {'class':'name'})
            icon = icon['value']
            unicode = div.find('input', {'class':'css'})
            unicode = unicode['value']
            self.unicodes[icon] = unicode

    def saveAsSass(self):
        sass_file = open('icons/ionicons/_ionicons.scss', 'wb')
        sass_file.write('$ionicons-icons: (')

        array = self.unicodes
        counter = 0
        icons = len(array)
        for icon, ucode in array.iteritems():
            counter +=1
            if counter == icons:
                sass_file.write("'%s': '%s'" % (icon, ucode))
            else:
                sass_file.write("'%s': '%s'," % (icon, ucode))

        sass_file.write(');')
        sass_file.close()

    def getText(self, parent):
        return ''.join(parent.find_all(text=True, recursive=False)).strip()