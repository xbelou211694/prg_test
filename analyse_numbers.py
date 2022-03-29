def is_natural_number(number):
    if number % 1 == 0 and number > 0:
        return True
    else:
        return False

def main():
    my_number = 5
    print(is_natural_number(my_number))

if __name__ == "__main__":
    main()

