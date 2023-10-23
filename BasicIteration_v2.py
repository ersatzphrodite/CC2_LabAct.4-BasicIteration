numbers = []

for i in range(7):
    while True:
        num = int(input(f"Enter number: "))
        numbers.append(num)
        break

print("Numbers =", numbers)

pair_found = False

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == 0:
            print(f"Pair/s found: ({numbers[i]}, {numbers[j]})")
            pair_found = True
            #   Removed the break statement after the "Pair found" message to continue checking for other pairs.

        if pair_found:
            continue

if not pair_found:
    print("No pair has the sum of 0.")
    #   Figure out how to remove loop in output if there are no pairs.
    #   Solution: moved if not pair_found outside the inner loop.
