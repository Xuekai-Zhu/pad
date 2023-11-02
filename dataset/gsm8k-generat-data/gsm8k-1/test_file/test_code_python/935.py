Unfortunately, we cannot provide the solution to the Samantha's last name problem as there is not enough information provided to determine the answer.

def solution():
    """Craig and his brother take turns spelling out the longest letter words they know and counting the number of the letters in those words. After ten rounds, Craig has spelled out 20 words with 15 letters each. If Craig's brother has spelled words with a total count of letters 50 more than Craig, calculate the total number of letters in the words they've spelled after the ten rounds."""
    craig_rounds = 10
    craig_words_per_round = 1
    craig_letters_per_word = 15
    craig_total_letters = craig_rounds * craig_words_per_round * craig_letters_per_word

    brother_total_letters = craig_total_letters + 50

    total_letters = craig_total_letters + brother_total_letters
    result = total_letters
    return result

print(solution())