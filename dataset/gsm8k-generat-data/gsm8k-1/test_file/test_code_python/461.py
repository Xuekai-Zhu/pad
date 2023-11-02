def solution():
    """Miss Maria is a middle school teacher, and she loves to collect sports cards. She has six decks with 25 basketball cards in each deck and five boxes with 40 baseball cards in each box. She keeps 50 cards and gives the remaining cards to her students. If her students got ten cards each, how many students does Miss Maria have?"""
    basketball_cards = 6 * 25
    baseball_cards = 5 * 40
    total_cards = basketball_cards + baseball_cards
    cards_left = total_cards - 50
    students = cards_left // 10
    result = students
    return result

print(solution())