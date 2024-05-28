weight = input("Enter the Weight: ")
height = input("Enter the Height: ")

#Weight and Height entered will be registered as Strings
#Therefore we define an another variable with the data type as float

w_as_float = float(weight)
h_as_float = float(height)


#Now we implement the formula for calculating BMI
#bmi = weight(kg) / height(m)^2

bmi = w_as_float/(h_as_float * h_as_float)

#We use the round function to get an whole number

print("The BMI is: ",round(bmi))

