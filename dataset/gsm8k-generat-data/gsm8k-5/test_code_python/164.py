def solution():
    # Buddy's baseball cards on Monday
    monday_cards = 30

    # Buddy's baseball cards on Tuesday after losing half
    tuesday_cards = monday_cards / 2

    # Buddy's baseball cards on Wednesday after buying 12
    wednesday_cards = tuesday_cards + 12

    # Buddy's baseball cards on Thursday after buying a third of what he had on Tuesday
    thursday_cards = tuesday_cards + (tuesday_cards / 3)

    result = thursday_cards
    return result

print(solution())