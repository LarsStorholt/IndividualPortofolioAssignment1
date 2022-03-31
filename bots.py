import random
import list_of_words

def meldingFraBot():
    return "Ellen: I can't answer that, sorry"


def ellen(word):
    if word in list_of_words.hello_list:
        response = random.choice(list_of_words.hello_list)
        return "Ellen: " + response

    elif word in list_of_words.verbs:
        response =  [
            f'Before becoming a chatbot, I was working as a sailer. I did a lot of {word + "ing"} back then',
            f'The chatbot Ellen is at duty. {word + "ing"} in Norwegian is torskelever',
            f'i would love to help you with {word + "ing"}',
            f'HAHAHAH! Are you kidding? Ellen which is my name, means hairy back in Chinese. {word + "ing"} is fun',
            f'Oh thats perfect! {word + "ing"} is my main field. I got a master degree in that'
        ]
        return "Ellen: " + random.choice(response)

def ola(word):
    if word in list_of_words.hello_list:
        response = random.choice(list_of_words.hello_list)
        return "Ola: " + response

    elif word in list_of_words.verbs:
        response = [
            f'I love {word + "ing"}, let`s go!',
            f'{word + "ing"}?? Are you serious?',
            f'{word + "ing"}. Isnt that illigal?',
            f'{word + "ing"}. I will rather {random.choice(list_of_words.verbs)}',
            f'Im the robot Ola, Im here to guidence you in {word + "ing"}',
        ]
        return "Ola: " + random.choice(response)

def ingrid(word):
    if word in list_of_words.hello_list:
        response = random.choice(list_of_words.hello_list)
        return "Ingrid: " + response

    elif word in list_of_words.verbs:
        response = [
            f'{word + "ing"} is exactly what I need now!',
            f'Im in the middle of something right now. i aint got time for helping you with {word + "ing"}',
            f'Jesus christ! Are you sure about that?  I have to shower first and take some pills. Then Im ready for {word + "ing"} ',
            f'My granma died last nigh. So I cannot {word + "ing"} today',
            f'I love to {word + "ing"} on mondays, but sundays are for resting'
        ]
    return "Ingrid: " + random.choice(response)

def steffen(word):
    if word in list_of_words.hello_list:
        response = random.choice(list_of_words.hello_list)
        return "Steffen: " + response
    elif word in list_of_words.verbs:
        response = [
            f'I would love to help you {word + "ing"}',
            f'My parents are out of town this weekend! {word + "ing"} sound perfect!',
            f'{word + "ing"}, running, eating, drinking and sleeping are my favorit activities',
            f'Hello Im a robot. You have to help yourself with {word + "ing"}',
            f'I cant help you with that. Ask my friend Ellen for {word + "ing"}'
        ]
        return "Steffen: " + random.choice(response)

