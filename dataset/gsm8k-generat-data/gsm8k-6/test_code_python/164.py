def solution():
    # Calculate the number of baseball cards Buddy has on Tuesday
    cards_on_tuesday = 30 / 2  # Buddy loses half of his cards on Tuesday

    # Calculate the total number of baseball cards Buddy has on Thursday
    cards_on_thursday = cards_on_tuesday + 12 + (cards_on_tuesday / 3)  # Buddy buys 12 cards on Wednesday and a third of what he had on Tuesday on Thursday

    result = cards_on_thursday
    return result

print(solution())