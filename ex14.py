from sys import argv

script, user_name = argv
prompt = "? "

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few question.")
print(f"{user_name}, do you like me?")
likes = input(prompt)

print(f"Where are you live {user_name}?")
live = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Ok, so you said \"{likes}\" about liking me.
you live in {live}. Not sure where that is.
And you have a {computer} computer. It's awesome.
""")