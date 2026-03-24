from calculator import add
def run():
    print("1) Subtract\n0)Exit")
    choice = input("Select")
    a = float(input("a: "))    
    b = float(input("b: "))
    print(add(a, b))