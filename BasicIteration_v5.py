numbers = []

print("▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩ INPUT UP TO 7 NUMBERS: ▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩")
#   Print outside of loop to only ask for input once.

max_input = 7  # Set the maximum number of inputs
#   while True: - irrelevant/if I keep it, `Enter` doesn't break the loop as intended.
for i in range(max_input):  # Only ask for up to 7 inputs.
    num = input(f"✔ Enter an integer (or press Enter to finish): ")
#   num = int(input(f"✔ "))
    # Changed "Enter number:" to check mark (✔) to avoid repetition of print statement.

    if not num:  # If the user presses Enter without entering a number
        break  # Exit the loop
    try:
        num = int(num)  # Convert the input to an integer
        if num not in numbers:  # Checks if num is not already in the set.
            numbers.append(num)
        else:
            print("You've already entered that number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number or press Enter to finish input.")

    if len(numbers) >= max_input:
        print("You've reached the maximum number of inputs (7).")
        break

print("▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩")

print("Numbers =", numbers)
print("Which pair/s of numbers have the sum of zero?")

pair_found = False

pairs = []

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == 0:
            # pair_found = True - `if not pair_found` is no longer in use so this serves no purpose.
            # break - Removed statement after `pair_found` to continue checking for other pairs.
            pairs.append((numbers[i], numbers[j]))
            # Used pairs.append to store pairs in a list instead of multiple line output in my initial submission.
#       if pair_found: - also irrelevant
#           continue - also irrelevant

#   if not pair_found: - Checks the boolean flag `pair_found` which is no longer in use.
#       print("No pair has the sum of 0.")
            # Figure out how to remove loop in output if there are no pairs.
            # Solution: moved `if not pair_found` outside the inner loop.

#   if pairs: - Checks if the pairs list is not empty. Easier to understand than `if not pair_found`.
#       print("Pairs found:", pairs) - Executes if pairs list = True (not empty).

if len(pairs) == 1:  # Checks if there's exactly one pair in the pairs list.
    print("✔ The pair", pairs[0], "has a sum of zero.")
elif pairs:  # Checks if there are multiple pairs.
    print("✔ The pairs", pairs, "have a sum of zero.")
else:
    print("✔ No existing pair has a sum of zero.")  # Executes if pairs list = False (empty).

print("▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩")
