# Danial Nijhout-Rowe
# 03/16/2025
# Assignment: List & Loop Practice

def main():
    # Step 1: Create your list 'numbers'
    numbers = []
    square_numbers = []
    for i in range(1,11):
        numbers.append(i)

    # Step 2: Loop through the list and print each number squared
    for num in numbers:
        print(num ** 2)
        square_numbers.append(num**2)


    # Step 3: Print the sum of the squared numbers
    sum = 0
    for num in square_numbers:
        sum += num
    print(sum)

    

if __name__ == "__main__":
    main()
