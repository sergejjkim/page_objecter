import re
import sys
import urllib3
import argparse

from lxml import etree

import write_elements

# todo add mobile shit
# todo make relative xpathes
# todo add h1, table, select
XML = "xml"
HTML = "html"

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("url_or_file", type=str, help="URL of a web page or path to file. Use -u --url if it's URL")
arg_parser.add_argument("class_name", type=str, help="Name of class to generate")
arg_parser.add_argument("-u", "--url", action="store_true", help="If specified - expecting URL in first argument")
arg_parser.add_argument("-f", "--file", type=str,
                        help="File name to write to. If not specified, file name is generated from class name")
arg_parser.add_argument("-p", "--parser", type=str, choices=[HTML, XML], default=XML,
                        help="Input source format, defaults to XML")

args = arg_parser.parse_args()


def get_page_source():
    global data
    if args.use_url:
        http = urllib3.PoolManager()
        r = http.request('GET', args.url_or_file)
        assert r.status == 200, "Response from site is not 200"

        return r.data

    else:
        with open(args.url_or_file, 'r') as html_source:
            return html_source.read().encode()


def camel_back_to_underscore(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


data = get_page_source()

if args.parser == HTML:
    parser = etree.HTMLParser()
elif args.parser == XML:
    parser = etree.XMLParser()
else:
    raise NotImplementedError("Unknown parser selected")

root = etree.fromstring(data, parser)

if len(sys.argv) >= 4:
    file_name = args.file
else:
    file_name = camel_back_to_underscore(sys.argv[2]) + ".py"

with open(file_name, "w+") as class_file:
    write_elements.write_imports(class_file)
    write_elements.write_class_name(args.class_name, class_file)
    write_elements.write_all_elements(root, class_file)
    write_elements.write_custom_elements(root, class_file)
