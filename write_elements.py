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


def get_element_name_raw(element_to_name):
    if NAME in element_to_name.attrib:
        return element_to_name.attrib.get(NAME)
    if ID in element_to_name.attrib:
        return element_to_name.attrib.get(ID)
    if TITLE in element_to_name.attrib:
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
    if "id" in element_to_form_selector_for.attrib:
        return "find_element_by_id('%s')" % element_to_form_selector_for.attrib.get("id")
    if "name" in element_to_form_selector_for.attrib:
        return "find_element_by_name('%s')" % element_to_form_selector_for.attrib.get("name")
    return "find_element_by_xpath('%s')" % etree.ElementTree(root_element).getpath(element_to_form_selector_for)


def write_imports(file):
    file.write(properties.a_import + "\n")
    for pattern in properties.custom_patterns:
        file.write(pattern.get(properties.ELEMENT_IMPORT) + "\n")
    file.write("\n\n")


def write_all_elements(root_element, file):
    for element in root_element.iter():
        if element.tag == "a":
            element_string = ELEMENT_STRING_PATTERN % (
                get_element_name(element),
                properties.static_text_tag_element.lower(),
                properties.a_tag_element,
                properties.driver_literal,
                form_selector(element, root_element))
            print(element_string)
            file.write(element_string)
        if element.tag == "UIAStaticText":
            element_string = ELEMENT_STRING_PATTERN % (
                get_element_name(element),
                properties.static_text_tag_element.lower(),
                properties.static_text_tag_element,
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