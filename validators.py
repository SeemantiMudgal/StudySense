def get_non_empty_input(message):
    while True:
        value = input(message).strip()

        if value:
            return value

        print("Input cannot be empty. Please try again.")


def get_positive_number(message):
    while True:
        try:
            value = float(input(message))

            if value > 0:
                return value

            print("Please enter a number greater than 0.")

        except ValueError:
            print("Please enter a valid number.")


def get_priority():
    while True:
        priority = input("Priority (Low/Medium/High): ").strip().capitalize()

        if priority in ["Low", "Medium", "High"]:
            return priority

        print("Please enter Low, Medium, or High.")