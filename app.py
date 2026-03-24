#simple console calculator
"""Console calculator entry point."""
from calculator import add
def main():
    print("1) Subtract\n0)Exit")
    choice = input("Select")
    a = float(input("a: "))    
    b = float(input("b: "))
    print(add(a, b))
    if choice == "2": print(sub(a, b))
    if option == "2": print(sub(a, b))
if __name__ == "__main__":
    main()
