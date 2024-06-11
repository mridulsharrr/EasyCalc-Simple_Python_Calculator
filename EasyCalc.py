def Greet():
    print("Welcome to EasyCalc a Simple Python Calculator")

Greet()


def ChooseOperator():
    while True:
        Operation = input("Print the operation: ")
        if Operation == "+" or "-"or "*"or"/":
            return Operation

def GetNumbers():
    num1 = int(input("What's your First number? "))
    num2 = int(input("What's your Second number? "))
    return num1 | num2



def main():
    print("Use (+)ADD  (-)SUBTRACT  (*)MULTIPLY  (/)DIVIDE")
    Operator = ChooseOperator()
    print("Operation Selected:", (Operator))
    GetNumbers()

main()