numbers = []

for i in range(7):
    while True:
        num = int(input(f"Enter number: "))
        numbers.append(num)
        break

pair_found = False

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == 0:
            print(f"Pair found: ({numbers[i]}, {numbers[j]})")
            pair_found = True
            break

        if pair_found:
            continue
        if not pair_found:
            print("No pair has the sum of 0.")
            #   figure out how to remove loop in output if there are no pairs
