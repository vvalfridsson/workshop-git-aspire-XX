#simple console calculator
"""Console calculator entry point."""
from calculator import add
def main():
    print("1) Add n\2 Subtract\n3) Multiply\n4) Divide\n0 Quit")
    option = input("Select: ")
    a = float(input("a: "))    
    b = float(input("b: "))
    print(add(a, b))
    if choice == "1": print("TODO Add")
    if option == "1": print("TODO Add")
if __name__ == "__main__":
    main()
