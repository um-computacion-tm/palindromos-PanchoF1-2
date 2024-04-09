import unittest

def is_palindrome(palabra):
    palabra = palabra.replace('','')
    reverse_string = palabra[::-1]
    if palabra.lower() == reverse_string.lower():
        return True
    return False


class Test_Palindromo(unittest.TestCase):
    def test_Palindromo_1(self):
        es_palindromo = is_palindrome("a")
        self.assertTrue(es_palindromo)

    def test_Palindromo_2(self):
        es_palindromo = is_palindrome("ala")
        self.assertTrue(es_palindromo)

    def test_Palindromo_3(self):
        es_palindromo = is_palindrome("neuquen")
        self.assertTrue(es_palindromo)

    def test_Palindromo_4(self):
        es_palindromo = is_palindrome("hola")
        self.assertFalse(es_palindromo)
    


unittest.main()