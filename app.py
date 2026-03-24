from calculator import add, sub
def run():
    print("1) Subtract\n0)Exit")
    choice = input("Select")
    a = float(input("a: "))    
    b = float(input("b: "))
    print(add(a, b))
    if choice == "2": print(sub(a, b))