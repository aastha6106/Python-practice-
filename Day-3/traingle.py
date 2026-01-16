side1 = float(input("Enter the first side of the traingle: "))
side2 = float(input("Enter the second side of the traingle: "))
side3 = float(input("Enter the third side of the traingle: "))

if side1 > 0 and side2 > 0 and side3 > 0:

    if(side1 + side2 > side3) and (side2 + side3 > side1) and (side1 + side3 > side2):
        print("Valid Traingle.")
    else:
        print("Invalid Traingle.")
else:
    print("Invalid Traingle. All sides mudt be positive.")