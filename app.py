#simple console calculator
"""Console calculator entry point."""
from calculator import add
def main():
    print("1) Add\n2) subtract\n3)Multiply\n4) Divide\n0) Exit program")
    choice = input("Select")
    a = float(input("a: "))    
    b = float(input("b: "))
    print(add(a, b))
    if choice == "4" and b == 0: print("Error: division by zero")
    if choice == "4" and b != 0: print (div(a, b))
if __name__ == "__main__":
    main()