xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]

# Print numbers

for num in xs:
    print(num)


# Each number and its square

for num in xs:
    square = num ** 2
    print(f"The square of {num} is {square}")

# Total of all numbers
total = 0
for num in xs:
    total += num

print(total)


# Print the product of all numbers
product = 1
for num in xs:
    product = product * num

print(product)
