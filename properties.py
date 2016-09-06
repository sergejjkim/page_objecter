from elements import ElementStuff

ELEMENT_IMPORT = "element_import"
ELEMENT = "element"
PATTERN = "pattern"

super_class_literal = "BasePage"
driver_literal = "driver"


static_text_tag_element = "Text"
static_text_import = "from elements import Text"

custom_patterns = [{PATTERN: ".//section/div[2]/div[a]",
                    ELEMENT: "custom_element1",
                    ELEMENT_IMPORT: "from custom_stuff import CustomElement1"},
                   {PATTERN: ".//input",
                    ELEMENT: "EditField",
                    ELEMENT_IMPORT: "from elements import EditField"}]


a = ElementStuff("a", "Button", "from elements import Button")

ios_text = ElementStuff("UIAStaticText", "Text", "from elements import Text")
ios_button = ElementStuff("UIAButton", "Button", "from elements import Button")
ios_img = ElementStuff("UIAImage", "Image", "from elements import Image")

elements = [ios_text, ios_button, ios_img]