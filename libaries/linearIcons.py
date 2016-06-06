import urllib
from bs4 import BeautifulSoup

class LinearIconsUnicodeResolver:
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
        divs = soup.findAll('div', { 'class': 'glyph fs1' })

        for div in divs:
            icon = div.find('span', {'class':'mls'})
            icon = icon.get_text().replace(" ", "")
            unicode = div.find('input', {'class':'unit'})
            unicode = unicode['value']
            self.unicodes[icon] = unicode

    def saveAsSass(self):
        sass_file = open('icons/linearicons/_linearicons.scss', 'w')
        sass_file.write('$linearicons-icons: (')

        array = self.unicodes
        counter = 0
        icons = len(array)
        for icon, ucode in array.iteritems():
            counter +=1
            if counter == icons:
                sass_file.write("'%s': '\%s'" % (icon, ucode))
            else:
                sass_file.write("'%s': '\%s'," % (icon, ucode))

        sass_file.write(');')
        sass_file.close()

    def getText(self, parent):
        return ''.join(parent.find_all(text=True, recursive=False)).strip()