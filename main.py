import re
import sys
import urllib3

from lxml import etree

import write_elements
import properties


# todo add mobile shit
# todo make relative xpathes
# todo add h1, table, select
# todo add argparses

print(sys.argv[1])
url_or_file = sys.argv[1]
class_name = sys.argv[2]


def get_page_source():
    global data
    if properties.use_url:
        http = urllib3.PoolManager()
        r = http.request('GET', url_or_file)
        assert r.status == 200, "Response from site is not 200"

        return r.data

    else:
        with open(url_or_file, 'r') as html_source:
            return html_source.read().encode()


def camel_back_to_underscore(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

data = get_page_source()

if properties.use_html:
    parser = etree.HTMLParser()
else:
    parser = etree.XMLParser()

root = etree.fromstring(data, parser)

if len(sys.argv) >= 4:
    file_name = sys.argv[3] + ".py"
else:
    file_name = camel_back_to_underscore(sys.argv[2]) + ".py"


with open(file_name, "w+") as class_file:
    write_elements.write_imports(class_file)
    write_elements.write_class_name(class_name, class_file)
    write_elements.write_all_elements(root, class_file)
    write_elements.write_custom_elements(root, class_file)
