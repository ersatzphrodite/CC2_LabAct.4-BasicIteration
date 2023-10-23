numbers = []

print("▩▩▩▩▩▩▩▩▩▩▩▩▩ INPUT 7 NUMBERS: ▩▩▩▩▩▩▩▩▩▩▩▩▩")  # Print outside of loop to only ask for input once.

for i in range(7):  # Only ask for 7 inputs.
    while True:
        num = int(input(f"✔ "))  # Changed "Enter number:" to check mark (✔) to avoid repetition of print statement.
        if num not in numbers:  # Check if num is not already in the set.
            numbers.append(num)
            break  # Stops when a unique number is entered.
        else:
            print("You've already entered that number. Please try again.")

print("▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩")

print("Numbers =", numbers)
print("Which pair/s of numbers have the sum of zero?")

pair_found = False

pairs = []

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == 0:
            #   pair_found = True (`if not pair_found` is no longer in use so this serves no purpose.)
            #   break   (Removed statement after `pair_found` to continue checking for other pairs.)
            pairs.append((numbers[i], numbers[j]))
            #   Used pairs.append to store pairs in a list instead of multiple line output in my initial submission.
        if pair_found:
            continue

#   if not pair_found: (Checks the boolean flag `pair_found` which is no longer in use.)
    #   print("No pair has the sum of 0.")
        #   Figure out how to remove loop in output if there are no pairs.
        #   Solution: moved if not pair_found outside the inner loop.

#   if pairs: (Checks if the pairs list is not empty. Easier to understand than `if not pair_found`.)
    #   print("Pairs found:", pairs)    # Executes if pairs list = True (not empty).

if len(pairs) == 1:  # Checks if there's exactly one pair in the pairs list.
    print("✔ Pair found:", pairs[0])  # Prints single pair with "Pair found:".
elif pairs:  # Checks if there are multiple pairs.
    print("✔ Pairs found:", pairs)
else:
    print("✔ No pair has the sum of zero.")  # Executes if pairs list = False (empty).

print("▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩")
