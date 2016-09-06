import re

from lxml import etree

import properties

ELEMENT_STRING_PATTERN = "\tdef get_%s_%s(self):\n\t\treturn %s(%s.%s)\n\n"

NAME_ME_PLEASE = "NAME_ME_PLEASE_I_CANT_DO_IT_MYSELF"
TITLE = "title"
ID = "id"
NAME = "name"


def write_class_name(class_name, file):
    class_string = "class %s(%s):\n\n" % (class_name, properties.super_class_literal)
    print(class_string)
    file.write(class_string)


def property_in_element(prop, element):
    return prop in element.attrib and element.attrib.get(prop)


def get_element_name_raw(element_to_name):
    if property_in_element(NAME, element_to_name):
        return element_to_name.attrib.get(NAME)
    if property_in_element(ID, element_to_name):
        return element_to_name.attrib.get(ID)
    if property_in_element(TITLE, element_to_name):
        return element_to_name.attrib.get(TITLE)
    if element_to_name.text:
        split = element_to_name.text.lower().split(maxsplit=4)
        if len(split) == 1:
            return split[0]
        elif len(split) == 2:
            return split[0] + "_" + split[1]
        elif len(split) >= 3:
            return split[0] + "_" + split[1] + "_" + split[2]
        else:
            return NAME_ME_PLEASE
    return NAME_ME_PLEASE


def get_element_name(element_to_name):
    raw_name = get_element_name_raw(element_to_name)
    if raw_name != NAME_ME_PLEASE:
        raw_name = re.sub(r'[\W]', '_', raw_name)
        return raw_name.replace(" ", "_").lower()
    return NAME_ME_PLEASE


def form_selector(element_to_form_selector_for, root_element):
    if property_in_element(ID, element_to_form_selector_for):
        return "find_element_by_id('%s')" % element_to_form_selector_for.attrib.get("id")
    if property_in_element(NAME, element_to_form_selector_for):
        return "find_element_by_name('%s')" % element_to_form_selector_for.attrib.get("name")
    return "find_element_by_xpath('%s')" % etree.ElementTree(root_element).getpath(element_to_form_selector_for)


def write_imports(file):
    imports_set = set()
    for page_element in properties.elements:
        imports_set.add(page_element.element_import)
    for pattern in properties.custom_patterns:
        imports_set.add(pattern.get(properties.ELEMENT_IMPORT))

    for line in imports_set:
        file.write(line + "\n")
    file.write("\n\n")


def write_all_elements(root_element, file):
    for element in root_element.iter():
        for page_element in properties.elements:
            if element.tag == page_element.tag_name:
                element_string = ELEMENT_STRING_PATTERN % (
                    get_element_name(element),
                    page_element.element_name.lower(),
                    page_element.element_name,
                    properties.driver_literal,
                    form_selector(element, root_element))
                print(element_string)
                file.write(element_string)


def write_custom_elements(root_element, file):
    for pattern in properties.custom_patterns:
        for element in root_element.findall(pattern.get(properties.PATTERN)):
            element_string = ELEMENT_STRING_PATTERN % (
                get_element_name(element),
                pattern.get(properties.ELEMENT),
                properties.driver_literal,
                form_selector(element, root_element))
            print(element_string)
            file.write(element_string)