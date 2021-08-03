weight = float(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print(f"Your weight is {converted} pounds.")
elif unit.upper() == "L":
    converted = weight * 0.45
    print(f"Your weight is {converted} kilos.")
else:
    print("Sorry! Input the correct unit name.")