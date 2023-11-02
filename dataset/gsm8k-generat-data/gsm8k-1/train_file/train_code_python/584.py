def solution():
    """Maddy's 4th grade class needs to make 1000 Valentine's Day cards to get a pizza party. There are 30 kids in the class. If everyone makes 8, how many more cards will they need to make to get a pizza party?"""
    cards_needed = 1000
    kids_in_class = 30
    cards_per_kid = 8
    cards_made = kids_in_class * cards_per_kid
    cards_remaining = cards_needed - cards_made
    result = cards_remaining
    return result

print(solution())