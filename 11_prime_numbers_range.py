start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("Prime numbers:")


for number in range(start, end + 1):
    if number < 2:
        continue

    is_prime = True

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(number, end=" ")

  Input
Enter starting number: 1
Enter ending number: 20

Output
Prime numbers:
2 3 5 7 11 13 17 19
