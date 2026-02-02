def odd_even(n):
    return "Even" if n%2 == 0 else "Odd"

def multiple(n,limit):
    return [i for i in range(n, limit+1,n)]
def square_cube(n):
    return n*n, n*n*n
print("===Number Utility Tool ===")
num = int (input("Enter a number: "))
print("1. Odd or Even")
print("2. multiples")
print("3.square & cube")

choice = int(input("choose a option 1-3: "))

if choice == 1:
    print(f"{num} is {odd_even(num)}")
elif choice == 2:
    limit = int(input("Enter a limit: "))
    print(f"{num} is {multiple(num, limit)}")
elif choice == 3:
    sq,cb = square_cube(num)
    print(f"Square is {sq}, Cube: {cb}")
else:
    print("Invalid choice")
