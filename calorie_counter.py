age = int("raw_input ("Please enter your age: "))
weight = int("raw_input ("Please enter your weight in pounds: "))
height = int("raw_input ("Please enter your height in inches: "))
gender = str("raw_input ("Please enter your gender, m for male and f for female: "))

bmi = weight / height / height * 703
male_bmr = 66.47 + (13.75 * weight) + (5.0 * height) - (6.75 * age)
female_bmr = 665.09 + (9.56 * weight) + (1.84 * height) - (4.67 * age)
bmr = male_bmr, female_bmr
if gender = "m" then bmr = male_bmr
  else bmr = female_bmr
  
print "\nYour BMI is %bmi and your required calorie intake is %bmr"

raw_input("\nPress the enter key to close the window.")
