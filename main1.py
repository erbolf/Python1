import logging

# Логду жөндөө
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

def get_user_age():
    logging.info("Жаш суроо функциясы башталды.")
    try:
        age_input = input("Жашыңызды киргизиңиз: ")
        age = int(age_input)
        logging.info(f"Колдонуучу киргизген жаш: {age}")
        print(f"Рахмат! Сиздин жашыңыз: {age}")
    except ValueError:
        logging.error("Ката! Колдонуучу сан эмес маалымат киргизди.")
        print("Сураныч, бир гана сан киргизиңиз!")

if __name__ == "__main__":
    logging.info("Программа ишке кирди.")
    get_user_age()
    logging.info("Программа ийгиликтүү аяктады.")

import unittest

def check_even(number):
    return number % 2 == 0

class TestLogic(unittest.TestCase):
    def test_is_even(self):
        self.assertTrue(check_even(4))
    
    def test_is_odd(self):
        self.assertFalse(check_even(3))

if __name__ == "__main__":
    unittest.main()

