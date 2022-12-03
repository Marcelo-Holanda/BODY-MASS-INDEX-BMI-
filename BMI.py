###Develop a logic that reads a person's weight and height,
###calculate your BMI and show your status, according to the table below;
### Under 18.5: Underweight / Between 18.5 and 25: Ideal Weight / 25 Up to 30: Overweight
### 30 to 40: Obesity / Over 40: Morbid Obesity



height = float(input('height:'))
weight = float(input('weight:'))
bmi = weight / (height*height)

if bmi < 18.5:
    print('CLASSIFICATION: Under weight')
elif 18.5 <= bmi < 25:
    print('CLASSIFICATION: Ideal weight')
elif 25 <= bmi < 30:
    print('CLASSIFICATION: about weight ')
elif 30 <= bmi < 40:
    print('CLASSIFICATION: Obesity')
elif bmi >= 40:
    print('CLASSIFICATION: Morbid obesity')