import random

name = "Lucy"
question = "Will it snow on Christmas?"
answer = ""

random_number = random.randint(1,12)
# print(random_number)

if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply Hazy, try again."
elif random_number == 5:
  answer = "Ask again Later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
elif random_number == 10:
  answer = "Perhaps."
elif random_number == 11:
  answer = 'Yes'
elif random_number == 12:
  answer = "No."
else:
  answer = "Error"

if name == "" and question != "":  
  print("Question: " + question)
  print("Magic 8-Ball's answer: " + answer)
elif question == "" and name != "":
  print(name + ", you did not ask a question!")
elif question == "" and name == "":
  print("No input has been given! Please try again.")
else:
  print(name + " asks: " + question)
  print("Magic 8-Ball's answer: " + answer)
