print("BMI calculator \n")
w=int(input("Enter your weight in kg: "))
h=float(input("Enter your height in meters:"))
bmi=w/(h*h)
print("Your BMI is: ",bmi)
if bmi<18.5:
 print("Your are underweight")

elif bmi>=18.5 and bmi<25:
 print("You have normal weight")

elif bmi>=25 and bmi<30:
 print("You are overweight")
else:
 print("You are obese")