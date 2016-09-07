

class OS(object):
    def __init__(self, name, element_structures, find_methods):
        self.name = name
        self.element_structures = element_structures
        self.find_methods = find_methods


class ElementStructure(object):
    def __init__(self, tag_name, element_name, element_import):
        self.tag_name = tag_name
        self.element_name = element_name
        self.element_import = element_import


class FindMethod(object):
    def __init__(self, element_property, driver_method):
        self.element_property = element_property
        self.driver_method = driver_method
