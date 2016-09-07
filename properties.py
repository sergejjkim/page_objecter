from elements import *

BY_NAME = "find_element_by_name"

RESOURCE_ID = "resource-id"

BY_ACCESSIBILITY_ID = "find_element_by_accessibility_id"

ACCESSIBILITY_IDENTIFIER = "accessibilityIdentifier"

BY_ID = "find_element_by_id"

IOS = "ios"
WEB = "web"
ANDROID = "android"
ELEMENT_IMPORT = "element_import"
ELEMENT = "element"
PATTERN = "pattern"

TITLE = "title"
ID = "id"
NAME = "name"

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

a = ElementStructure("a", "Button", "from elements import Button")

elements_web = [a]

ios_text = ElementStructure("UIAStaticText", "Text", "from elements import Text")
ios_button = ElementStructure("UIAButton", "Button", "from elements import Button")
ios_img = ElementStructure("UIAImage", "Image", "from elements import Image")

elements_ios = [ios_text, ios_button, ios_img]

elements_android = []

web_by_id = FindMethod(ID, BY_ID)
web_by_name = FindMethod(NAME, BY_NAME)

find_methods_web = [web_by_id, web_by_name]

ios_by_id = FindMethod(NAME, BY_ID)
ios_by_accessibility_id = FindMethod(ACCESSIBILITY_IDENTIFIER, BY_ACCESSIBILITY_ID)

find_methods_ios = [ios_by_accessibility_id, ios_by_id]

android_by_id = FindMethod(RESOURCE_ID, BY_ID)
android_by_name = FindMethod(NAME, BY_NAME)

find_methods_android = [android_by_id, android_by_name]


ios = OS(IOS, elements_ios, find_methods_ios)

android = OS(ANDROID, elements_android, find_methods_android)

web = OS(WEB, elements_web, find_methods_web)
