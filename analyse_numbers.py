def is_natural_number(number):
    is_natural = []
    for i in range(len(number)):
        if i % 1 == 0 and i > 0:
            is_natural.append(True)
        else:
            is_natural.append(False)

    return is_natural


def is_even_number(number):
    is_even = []
    for i in range(len(number)):
        if i % 2 == 0:
            is_even.append(True)
        else:
            is_even.append(False)
    return is_even


def main():
    my_numbers = [0, 2, 8, 7.4]
    print(is_natural_number(my_numbers))
    print(is_even_number(my_numbers))

if __name__ == "__main__":
    main()

