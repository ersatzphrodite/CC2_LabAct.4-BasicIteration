print("▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩ INPUT 7 NUMBERS: ▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩")
numbers = []
for i in range(7): 
    while True:
        try: 
            num = int(input(f"✔ "))  
            numbers.append(num)
            break  
        except ValueError:
            print("Please enter an integer")
print("▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩")
print("Numbers =", numbers)
print("Which pair/s of numbers have the sum of zero?")

pair_found = False
pairs = []

for i in numbers:
    for j in numbers:
        if i != j:
            ijsum = i + j
            if ijsum == 0:
                pair_found = True
                print(f"The sum of the pair ({i}, {j}) is 0")
                pairs.append((i, j))

if len(pairs) == 1:  
    print("✔ The pair", pairs[0], "has a sum of zero.")
elif pairs:  
    print("✔ The pairs", pairs, "have a sum of zero.")
else:
    print("✔ No existing pair has a sum of zero.")  
print("▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩")
