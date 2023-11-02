def solution():
    # Calculate the total number of doubles in Rob's collection
    jess_doubles = 40
    rob_doubles = jess_doubles / 5

    # Calculate the total number of cards in Rob's collection
    total_cards = rob_doubles / (1/3)

    # Calculate the number of non-doubles in Rob's collection
    non_doubles = total_cards - rob_doubles

    # Calculate the total number of cards Rob has
    rob_cards = non_doubles + rob_doubles
    result = rob_cards
    return result

print(solution())