print
"this program if for calculating your Body Mass Index BMI"
name = input('please enter your name: ')
weight  = float(input('please enter your body weight in KG; '))
height = float(input('pleae enter your height in Meters; '))
print
"we will proceed hoping the inputed information is accurate!"
mul = (height*height)

BMI = (weight/mul)

#print BMI

if(BMI>= 18.5 and BMI<= 24.9):
        print("")
        print (name," you have a good body mass index ratio")
        print("you have a moderate equivalence between your height and weight")
elif(BMI >= 25 and BMI <= 29.9):
        print("")
        print (name," you are overweight")
        print('since you cannot change your heigth i would advice you to cut down on junks and unnecesary food to bring down your weight')
elif(BMI < 18.5):
        print('')
        print (name,' you are underweight')
        print('please try to consume more and getting adequate rest is adviced to live healthier and vitamin supliments in little doses can be adviced o be taken')
        print('KEY NOTE SEE THE DOCTOR FOR BETTER AND HEALTHIER SUGGESTIONS')
else:
        print('')
        print (name,' you are OBESE')
        print ('you need to see the doctor fast! make an appointment today')


        
print('')
print('')
print('Thanks for using AYOMIKUNS BMI calculator have a nice day')
print('An healthy weight supports healthy living ;-)' )
        
