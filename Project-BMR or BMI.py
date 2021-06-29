name = input("Name?: ")
print(f"Hi, {name}!")

age_ask = input("Are you know your age?(y/n): ").lower()
if age_ask == "y":
    age = int(input("Age: "))
elif age_ask == "n":
    birth_year = input("Birth year: ")
    current_year = input("Current year: ")
    age = int(current_year) - int(birth_year)
    print(f"Your age is {age}")
else:
    print("I don't understand your command.")

height_ask = input("Are you know your height?(y/n): ").lower()
if height_ask == "y":
    height = int(input("Height: "))
elif height_ask == "n":
    height = int(input("Height: "))
    unit = input("(i)nch or (c)m: ").lower()
    if unit == "i":
        converted = height / 2.54
        print(f"You're {converted} inch")
    elif unit == 'c':
        converted = height * 2.54
        print(f"You're {converted} cm")
    else:
        print("I don't understand your command.")
else:
    print("I don't understand your command.")

weight_ask = input("Are you know your weight?(y/n): ").lower()
if weight_ask == "y":
    weight = int(input("Weight: "))
elif weight_ask == "n":
    weight = int(input("Weight: "))
    unit = input("(l)bs or (k)g: ").lower()
    if unit == "l":
        converted = weight / .45
        print(f"You're {converted} pounds")
    elif unit == "k":
        converted = weight * .45
        print(f"You're {converted} kg")
    else:
        print("I don't understand your command.")
else:
    print("I don't understand your command.")
# bmr
gender = input("Gender(m/f): ").lower()

if gender == 'm':
    bmrM = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
    print(f"Your Basal Metaloic Rate(BMR) value is {bmrM}")
elif gender == 'f':
    bmrF = (655 + (9.6 * weight) + (1.8 * height) - (4.7 * age))
    print(f"Your Basal Metaloic Rate(BMR) value is {bmrF}")
else:
    print("I don't understand your command.")
