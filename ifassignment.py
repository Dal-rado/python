the_height = float (input("Enter height in cm:"))
the_weight = float (input("Enter the weight in kg:"))

the_BMI= the_weight/(the_height/100)**2
print("Your body mass index is", the_BMI)

if the_BMI<=18.5:
    print("Oops!You are underweight")
elif the_BMI<=24.9:
    print("Awesome ! you are healthy")
elif the_BMI<=29.9:
    print("Eee ! you are overweight .LOOK FOR A GYM SUBSCRIPTION!!")
else :
    print("Seesh ! You are obese.")