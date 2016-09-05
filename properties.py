ELEMENT_IMPORT = "element_import"
ELEMENT = "element"
PATTERN = "pattern"

use_url = False
use_file = not use_url
use_html = False

super_class_literal = "BasePage"
driver_literal = "driver"

a_tag_element = "Button"
a_import = "from elements import Button"

static_text_tag_element = "Text"
static_text_import = "from elements import Text"

custom_patterns = [{PATTERN: ".//section/div[2]/div[a]",
                    ELEMENT: "custom_element1",
                    ELEMENT_IMPORT: "from custom_stuff import CustomElement1"},
                   {PATTERN: ".//input",
                    ELEMENT: "EditField",
                    ELEMENT_IMPORT: "from elements import EditField"}]
