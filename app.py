ERR_DIV_ZERO = "Error: division by zero"
#simple console calculator
"""Console calculator entry point."""
from calculator import add
def main():
    print("1) Subtract\n0)Exit")
    choice = input("Select")
    a = float(input(...))    
    b = float(input(...))
    a = float(input("a: "))    
    b = float(input("b: "))
    print(add(a, b))
    if option == "3": print(mul(a, b))
    if option == "4" and b == 0: print("ERR_DIV_ZERO")
if __name__ == "__main__":
    main()
