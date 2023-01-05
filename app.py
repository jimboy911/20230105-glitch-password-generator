from flask import Flask, render_template
import random

# Create a Flask app instance
app = Flask(__name__)

def passwordGenerator():
  #generate random number and print it out
  myNumber = random.randint(100000000000000, 999999999999999)

  #convert number into an integer array and print it out
  numberArray = map(int, str(myNumber))

  #establish all the possible characters in your password
  specialChar = "!@#$%^&*()-=+_"
  numbers = "01234567890"
  upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  lowerCase = "abcdefghijklmnopqrstuvwxyz"
  myPassword = []

  #determines what type of character to randomly generate
  for x in numberArray:
      if x in range(1,2):
          myPassword.append(random.choice(specialChar))

      elif x in range(3,5):
          myPassword.append(random.choice(upperCase))

      elif x in range(6,8):
          myPassword.append(random.choice(lowerCase))

      else:
          myPassword.append(random.choice(numbers))

  #convert list into string by joining all the elements of the string together
  finalPassword = ''.join(myPassword)
  return finalPassword

@app.route('/') #if i remove this - it stops working
@app.route('/index') #not sure why i have to add this to get it to readd my index.html file correctly.
def index():
    list_of_passwords = "List of Passwords Here!"
    return render_template(
      'index.html', 
      title='Password Generator v2.0', 
      password_1=passwordGenerator(), 
      password_2=passwordGenerator(), 
      password_3=passwordGenerator(), 
      password_4=passwordGenerator(), 
      password_5=passwordGenerator()
    )
#to get the html template to print the passwords on different lines, i had to create 5 different variables that ran the password generator function multiple times.
#there might be a way to do this cleaner
#looks like you can separate them onto different lines of code like this so it's easier to read
  
if __name__ == '__main__':
    app.run()