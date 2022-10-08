weight = int(input("Enter your weight in Kilograms:"));
height = float(input("Enter your height in meters:"));
x = weight/float(height*height);
if x < 18.5:
    print('Underweight')
else if x>=18.5 and x<25:
    print("Normal")
else if x >= 25 and x < 30:
   print('Overweight')
else:
   print('Obesity')
#use of if-else ladder
#reducing execution time
