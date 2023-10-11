#A função str_to_bool() recebe uma cadeia de caracteres como entrada e seu trabalho é retornar
# True ou False dependendo do conteúdo da cadeia de caracteres. Por exemplo, se a cadeia
# de caracteres for y, ela retornará True. Da mesma forma, se a cadeia de caracteres for no,
# ela retornará False.

import unittest

def str_to_bool(value):
    try:
        value = value.lower()
    except AttributeError:
        raise AttributeError(f"{value} must be of type string")
    #value = value.lower()#
    true_values = ['y','yes']
    false_values = ['no', 'n']

    if value in true_values:
        return True
    if value in false_values:
        return False
    
class TestStrToBool(unittest.TestCase):

    def test_y_is_true(self):
        result = str_to_bool('y')
        self.assertTrue(result)

    def test_yes_is_true(self):
        result = str_to_bool('Yes')
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
    
def test_invalid_input(self):
        with self.assertRaises(AttributeError):
            str_to_bool(1)