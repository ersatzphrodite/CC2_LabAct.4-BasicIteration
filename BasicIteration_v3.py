numbers = []

for i in range(7):
    while True:
        num = int(input(f"Enter number: "))
        numbers.append(num)
        break

print("Numbers =", numbers)

pair_found = False

pairs = []

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == 0:
            #   pair_found = True (if not pair_found is no longer in use so this serves no purpose.)
            #   break   (Removed statement after the "Pair found" message to continue checking for other pairs.)
            pairs.append((numbers[i], numbers[j]))
            #   Used pairs.append to store pairs in a list instead of multiple line output in my initial submission.
        if pair_found:
            continue

#   if not pair_found: (Checks the boolean flag pair_found which is no longer in use.)
    #   print("No pair has the sum of 0.")
        #   Figure out how to remove loop in output if there are no pairs.
        #   Solution: moved if not pair_found outside the inner loop.

if pairs:   # Checks if the pairs list is not empty. Easier to understand than if not pair_found.
    print("Pairs found:", pairs)    # Executes if pairs list = True (not empty).
else:
    print("No pair has the sum of 0.")  # Executes if pairs list = False (empty).
