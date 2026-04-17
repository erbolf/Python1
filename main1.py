import logging
def get_user_age(age_input):
    try:
        age = int(age_input)
        logging.info(f"Жаш: {age}")
        return age
    except:
        logging.error("Ката")
        return None


if __name__ == "__main__":
    user_input = input("Жаш: ")
    get_user_age(user_input)