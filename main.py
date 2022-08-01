def prime_checker(number):

    divider_list = []

    for num in range(1, number + 1):
        if number % num == 0:
            num = str(num).split()
            divider_list += num

    if len(divider_list) == 2:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


check_another = True

while check_another:
    n = int(input("Check this number: "))
    prime_checker(number=n)

    another_number = input("Would you like to check a different number? (yes/no) ")
    if another_number == "no":
        break
