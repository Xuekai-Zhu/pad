def solution():
    """In a set of magicians cards, there are 15 red cards, and 60% more green cards. Yellow cards are as many, as the sum of red and green cards. How many cards of all mentioned colors are there?"""
    red_cards = 15
    green_cards = red_cards * 1.6
    yellow_cards = red_cards + green_cards
    total_cards = red_cards + green_cards + yellow_cards
    result = total_cards
    return result

Note: For the Samantha's last name question, there is not enough information given to solve for the number of letters in Samantha's last name.

print(solution())