name = input("Enter your first name: ")
weight = int(input("Enter your weight in pounds: "))

Height = int(input("Enter your height in inches: "))
Bmi = (weight * 703) / (Height * Height)

print("Your BMI is: " + str(Bmi))

if Bmi>0:
    if Bmi<18.5:
        print(name + ", you are underweight")
    elif Bmi>20:
        print(name +  ", you are overweight")
else:
    print("Enter a Valid Number")