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
    
    def test_Palindromo_5(self):
        es_palindromo = is_palindrome("NeuQuen")
        self.assertTrue(es_palindromo)
    

    def test_Palindromo_6(self):
        es_palindromo = is_palindrome("salas")
        self.assertTrue(es_palindromo)


    def test_Palindromo_7(self):
        es_palindromo = is_palindrome("OsO")
        self.assertTrue(es_palindromo)

    def test_Palindromo_8(self):
        es_palindromo = is_palindrome("OJO")
        self.assertTrue(es_palindromo)

    def test_Palindromo_9(self):
        es_palindromo = is_palindrome("ANa")
        self.assertTrue(es_palindromo)

    def test_Palindromo_10(self):
        es_palindromo = is_palindrome("neuquen")
        self.assertTrue(es_palindromo)
    

    def test_Palindromo_11(self):
        es_palindromo = is_palindrome("NeuQuen")
        self.assertTrue(es_palindromo)
    

    def test_Palindromo_12(self):
        es_palindromo = is_palindrome("salas")
        self.assertTrue(es_palindromo)

unittest.main()