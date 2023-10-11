def char_freq(text):

  uppercase_frequency ={}
  lowercase_frequency ={}
  
  for char in text:
    if char.isalpha():
      
      if char.islower(): #Counting the lower case
        if char in lowercase_frequency:
          lowercase_frequency[char] += 1
        else:
          lowercase_frequency[char] = 1
      else: #Counting the upper case
        if char in uppercase_frequency:
          uppercase_frequency[char] += 1
        else:
          uppercase_frequency[char] = 1
  return uppercase_frequency, lowercase_frequency


# Print to introduce user to the frequency calculator
print("Welcome to the character frequency calculator.")


# Display the results

while True:
  #Get the user input the text they want to be calculated
  input_text = input("Please input your text here to calculate your result: ")
  #Get the user input on what type of character they would like to calculate
  inputanswer = input("Calculate in captial, lower case or both? (c/l/b)")
  uppercase_result, lowercase_result = char_freq(input_text)
  #If the user want to have captial letters only
  if inputanswer == "c":
    print(uppercase_result)
    #ask the user if they would like to use a different sentence
    #if user said no, the program ends
    while True:
      input_repeat = input("would you like to try a different sentence? (y/n)")
      if input_repeat == "y":
        print ("Thank you!")
        break
      elif input_repeat == "n":
        print ("Thank you for using the Frequency calculator")
        exit()
      else:
        print ("Please enter y or n")
        continue
  #if the user only wants lower case letters
  elif inputanswer == "l":  
    print(lowercase_result)
    #ask the user if they would like to use a different sentence
    #if user said no, the program ends
    while True:
      input_repeat = input("would you like to try a different sentence? (y/n)")
      if input_repeat == "y":
        print ("Thank you!")
        break
      elif input_repeat == "n":
        print ("Thank you for using the Frequency calculator")
        exit()
      else:
        print ("Please enter y or n")
        continue
  #if the user wants both lower and upper case calculated  
  elif inputanswer == "b":
    print(uppercase_result, lowercase_result)
    #ask the user if they would like to use a different sentence
    #if user said no, the program ends
    while True:
      input_repeat = input("would you like to try a different sentence? (y/n)")
      if input_repeat == "y":
        print ("Thank you!")
        break
      elif input_repeat == "n":
        print ("Thank you for using the Frequency calculator")
        exit()
      else:
        print ("Please enter y or n")
        continue
  else:
    #Ask the user to try again
    print("Invalid input. Please input your text again with the valid option")

