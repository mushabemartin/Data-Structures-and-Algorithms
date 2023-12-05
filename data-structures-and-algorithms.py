# Stacks

def is_balanced(expression):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or stack.pop() != brackets[char]:
                return False

    return not stack


# Sequences (Lists/Tuples)

def remove_duplicates(sequence):
    seen = set()
    result = []
    for item in sequence:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result


# Dictionaries

import string

def word_frequency(sentence):
    word_count = {}
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    words = sentence.lower().split()

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    return word_count


# Test cases

expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False

input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]

sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
