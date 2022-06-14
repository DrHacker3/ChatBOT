#Definitions
def hi():
    print("Hi", name)

def howyou():
    print("I'm doing great", name)

def should():
    print("That is entirely your decision", name)

def weather():
    print("Take a look outside or google it")
    print("I'm not your personal assistant")

def bored():
    print("Sucks to be you")

def boring():
    print("I know right")

def meet():
    print("No thanks")

def will():
    print("No")

def ok():
    print("No probs")

print("Hello, I am ChatBOT. Your digital friend!")
print("What is your name?")
name = input("Name: ")
print("Good to meat you", name)
while True:
    resp = input("> ").lower()
    if 'hello' in resp:
        hi()
    
    elif 'hi' in resp:
        hi()

    elif 'hey' in resp:
        hi()

    elif 'how are you' in resp:
        howyou()

    elif 'how you doing' in resp:
        howyou()

    elif 'should' in resp:
        should()

    elif 'weather' in resp:
        weather()

    elif 'bored' in resp:
        bored()

    elif 'boring' in resp:
        boring()

    elif 'meet' in resp:
        meet()

    elif 'will you' in resp:
        will()

    elif 'ok' in resp:
        ok()

    else:
        print("I dunno")
