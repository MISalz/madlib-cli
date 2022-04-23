
print(""""
Welcome to Mad Libs
Lets Play a game
Type in two adjectives and one noun
A Madlib response will be displayed.

**An adjective denotes a descriptive word that illustrates the noun used in a sentence.
**A noun is a word that connotes a particular name, place, idea, or object.
      """)


def read_template(path):
    try:
        with open(path,'r') as story:
            return story.read()
    except FileNotFoundError:
        raise FileNotFoundError


def parse_template(template):
    print(template)
    expected_stripped = "It was a {} and {} {}."
    expected_parts = ("Adjective", "Adjective", "Noun")
    return expected_stripped, expected_parts

	# r"(?<=\{)(.*?)(?=\})"
	# {(.*?)}
    # r'{[^}]*}'


def merge():
    # if path == "hi":
       print('FileNotFoundError')

