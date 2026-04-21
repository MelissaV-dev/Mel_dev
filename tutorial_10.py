# Student Name: Melissa Vaziri
# Student Number: #101366349

# Creating a variable called "vowels" and assigning all vowels to a list
vowels = ["a", "e", "i", "o", "u"]

# Creating the first function for "iteration"
# Type hinting is used to indicate that the function takes a list of strings as input
# and also specifies that it will return a list of strings.

def iterative(chars: list[str]) -> list[str]:
    # Creating a variable for the result as an empty list
    result = []

    # Start a loop to check each character.
    # If the character is a vowel, append its uppercase version to the result.
    # Otherwise, append the character as is.

    for ch in chars:
        if ch.lower() in vowels:
            result.append(ch.upper())
        else:
            result.append(ch)
            #this returns the final result after analyzing all the characters.
    return result

# The second function is recursive.
# It checks if the list of characters is empty, and if so, returns an empty list.

def recursive(chars: list[str]) -> list[str]:
    if len(chars) == 0:
        return []

    # Assign the first character to a variable.
    # If it is a vowel, make it uppercase;
    # if not, keep it as is.

    first_vowel = chars[0].upper() if chars[0].lower() in vowels else chars[0]

    # Combine the first character with the recursive result of the remaining characters.
    return [first_vowel] + recursive(chars[1:])

# Test whether the current character is a vowel
test_vowels = ["a", "e", "i", "o", "u"]

# performing another test for non-vowels
testing_non_vowels = ["m", "f", "h", "j", "l"]


# display both functions using test vowels
print(iterative(test_vowels))
print(recursive(test_vowels))

#printing the second test for non-vowels

print(iterative(testing_non_vowels))
print(recursive(testing_non_vowels))


#calling the functions
iterative(test_vowels)
recursive(test_vowels)