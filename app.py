#simple console calculator
"""Console calculator entry point."""
from calculator import add
def main():
    print("1) Add n\2 Subtract\n3) Multiply\n4) Divide\n0 Quit")
    option = input("Select: ")
    a = float(input("a: "))    
    b = float(input("b: "))
    print(add(a, b))
    if option == "3": print(mul(a, b))
    if option == "4" and b == 0: print("Error: division by zero")
if __name__ == "__main__":
    main()
