def solution():
    
    cards_needed = 1000
    kids_in_class = 30
    cards_per_kid = 8
    cards_made = kids_in_class * cards_per_kid
    cards_remaining = cards_needed - cards_made
    result = cards_remaining
    return result

print(solution())