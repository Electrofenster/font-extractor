# font-extractor
This script extracts all icons from FontAwesome, Ionicons and Linearicons and saves all icons as map

### requirements and installing
To get the script working you need https://pypi.python.org/pypi/beautifulsoup4

### running
To get the SASS files simple run
```bash
python get.py
```

### usage
simple import the files like this:
```sass
@import 'icons/fontawesome/fontawesome';
@import 'icons/ionicons/ionicons';
@import 'icons/linearicons/linearicons';
```

to get the right icon in sass you can use this
```sass
content: map-get($fontawesome-icons:, 'fa-camera'); // and you'll get \f030
```