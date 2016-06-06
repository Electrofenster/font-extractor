import urllib
from bs4 import BeautifulSoup

class FontAwesomeUnicodeResolver:
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
        divs = soup.findAll('div', { 'class': 'col-md-4 col-sm-6 col-lg-3' })

        for div in divs:
            icon = self.getText(div)
            unicode = div.findAll('span', {'class': 'text-muted'})[-1].get_text().replace('[&#x', '').replace(';]', '')
            self.unicodes[icon] = unicode

    def saveAsSass(self):
        sass_file = open('icons/fontawesome/_fontawesome.scss', 'w')
        sass_file.write('$fontawesome-icons: (')

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