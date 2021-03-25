#!/usr/bin/env python3

# Michael Barbas CSC437

inputStack = [] #stack
entry = "" #input
index = 0 #stack index

def takeInput():
    global entry
    entry = input("Enter a number or operator: ")

    if type(entry == "class 'str'"):
        entry.lower()

    calculate()

def calculate():
    global entry
    while entry != "exit":
        try:
            index = len(inputStack)
            if entry == "exp":
                if index >= 2:

                    inputStack.append(inputStack.pop() ** inputStack.pop())

                    index = len(inputStack)

                    for i in range(index):
                        print(str(i) + ": " + str(inputStack[index - 1]))
                        i += 1
                        index -= 1

                    index = len(inputStack) #annoying, is there a way to avoid repetition?

                    entry = input("Enter a number or operator: ").lower()
                else:
                    print("Needs more than one value to use EXP")
                    entry = input("Enter a number or operator: ").lower()

            elif entry == "chs":
                if index >= 1:

                    inputStack.append(inputStack.pop() * -1)

                    index = len(inputStack)

                    for i in range(index):
                        print(str(i) + ": " + str(inputStack[index - 1]))
                        i += 1
                        index -= 1

                    index = len(inputStack)

                    entry = input("Enter a number or operator: ").lower()
                else:
                    print("Needs at least one value to change sign")
                    entry = input("Enter a number or operator: ").lower()

            elif entry == "+":
                if index >= 2:

                    inputStack.append(inputStack.pop() + inputStack.pop())

                    index = len(inputStack)

                    for i in range(index):
                        print(str(i) + ": " + str(inputStack[index - 1]))
                        i += 1
                        index -= 1
                    index = len(inputStack)
                    entry = input("Enter a number or operator: ").lower()
                else:
                    print("Needs more than one value to add")
                    entry = input("Enter a number or operator: ").lower()


            elif entry == "-":
                if index >= 2:
                    
                    inputStack.append(inputStack.pop() - inputStack.pop())

                    index = len(inputStack)

                    for i in range(index):
                        print(str(i) + ": " + str(inputStack[index - 1]))
                        i += 1
                        index -= 1
                    index = len(inputStack)
                    entry = input("Enter a number or operator: ").lower()
                else:
                    print("Needs more than one value to subtract")
                    entry = input("Enter a number or operator: ").lower()


            elif entry == "/":
                if index >= 2:

                    inputStack.append(inputStack.pop() / inputStack.pop())

                    index = len(inputStack)

                    for i in range(index):
                        print(str(i) + ": " + str(inputStack[index - 1]))
                        i += 1
                        index -= 1
                    index = len(inputStack)
                    entry = input("Enter a number or operator: ").lower()
                else:
                    print("Needs more than one value to divide")
                    entry = input("Enter a number or operator: ").lower()

            elif entry == "*":
                if index >= 2:

                    inputStack.append(inputStack.pop() * inputStack.pop())

                    index = len(inputStack)

                    for i in range(index):
                        print(str(i) + ": " + str(inputStack[index - 1]))
                        i += 1
                        index -= 1

                    index = len(inputStack)

                    entry = input("Enter a number or operator: ").lower()
                else:
                    print("Needs more than one value to multiply")
                    entry = input("Enter a number or operator: ").lower()

            else:
                inputStack.append(float(entry))

                index = len(inputStack)

                for i in range(index):
                    print(str(i) + ": " + str(inputStack[index-1]))
                    i += 1
                    index -= 1

                i = 0;

                index = len(inputStack)
                takeInput()

        except ValueError:
            print("I dont think you meant to type that... typo maybe?? Try AGAIN")
            takeInput()
            continue
        except OverflowError:
            print("I think you got a little carried away, please restart...")


def main():
    print("Enter number values (int or float) and they will\n"
          "be added to the stack, once added perform either\n"
          "EXP (exponentiation), CHS (change sign), +, -, /, *, and EXIT\n"
          "It will perform these operations on the latest number(s) in stack...\n\n"
          "Have fun!\n-Michael\n")

    takeInput()

if __name__ == "__main__":
    main()



