"""
Intro to python exercises shell code
"""

def is_odd(x):
    """
    returns True if x is odd and False otherwise
    """
    
    return (x % 2 != 0)


def is_palindrome(word):
    """
    returns whether `word` is spelled the same forwards and backwards
    """

    return word == word[::-1]

def only_odds(numlist):
    """
    returns a list of numbers that are odd from numlist

    ex: only_odds([1, 2, 3, 4, 5, 6]) -> [1, 3, 5]
    """
    odds = list()
    
    for i in numlist:
        if is_odd(i):
            odds.append(i)

    return odds
            
def count_words(text):
    """
    return a dictionary of {word: count} in the text

    words should be split by spaces (and nothing else)
    words should be converted to all lowercase

    ex: count_words("How much wood would a woodchuck chuck"
                    " if a woodchuck could chuck wood?")
        ->
        {'how': 1, 'much': 1, 'wood': 1, 'would': 1, 'a': 2, 'woodchuck': 2,
        'chuck': 2, 'if': 1, 'could': 1, 'wood?': 1}
    """
    d = dict()
    
    words = text.split(" ")
    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
                
    return d

"""
print(is_odd(3))
print(is_odd(4))

print(is_palindrome("racecar"))
print(is_palindrome("python"))

print(only_odds([1, 2, 3, 4, 5, 6]))

c = count_words("How much wood would a woodchuck chuck if a woodchuck could chuck wood?")
print(c)
"""