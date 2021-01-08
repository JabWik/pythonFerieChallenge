# pythonFerieChallenge - Day 1
# reversed strings, palindromes & anagrams
# by Wiktoria Jabłońska

import webbrowser


def reverse_string(x):
    return x[::-1]


def check_if_palindrome(x):
    x = delete_punctation(x)
    x = x.casefold()
    y = reverse_string(x)

    if list(x) == list(y):
        print("\nMoreover, your string is a palindrome! (ﾉ◕ヮ◕)ﾉ*.✧")
    else:
        print("\nMoreover, your string is not a palindrome... ･ﾟ･(╥﹏╥)･ﾟ･")


def delete_punctation(x):
    punctations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    no_punctation = ""

    for char in x:
        if char not in punctations:
            no_punctation += char

    return no_punctation


if __name__ == '__main__':
    website = "https://poocoo.pl/scrabble-slowa-z-liter/"

    string = input("Please, input your string!\n")
    print("\n\nThis is what you wrote...\n", string)

    anagram = reverse_string(string)

    print("\n...and this is how it looks reversed!\n", anagram)

    check_if_palindrome(string)

    print("Now, it is a time for some fun! Let's open a web browser!!!")

    string = delete_punctation(string)
    webbrowser.open(website + string)
