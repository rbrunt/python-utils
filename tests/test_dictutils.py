from unittest import TestCase
import brunt_pyutils.dictutils


class TestDictUtils(TestCase):
    def test_can_traverse_dictionary(self):

        dictionary = {
            "this": "val",
            "parent": {
                "child": "interesting value"
            },
            "test[parent]": "valueue"
        }

        simple_value = brunt_pyutils.dictutils.traverse_dictionary(dictionary, "this")
        value = brunt_pyutils.dictutils.traverse_dictionary(dictionary, "parent.child", separator=".")
        list_value = brunt_pyutils.dictutils.traverse_dictionary(dictionary, ["parent","child"])

        self.assertEqual(simple_value, "val")
        self.assertEqual(value, "interesting value")
        self.assertEqual(list_value, "interesting value")
