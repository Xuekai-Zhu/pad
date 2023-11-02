def solution():
    initial_cards = 130
    keep_cards = 15
    num_friends = 8
    cards_per_friend = 12
    sisters_num = 2
    sisters_cards = 3

    # Calculate the total number of cards given away
    total_given = initial_cards - keep_cards

    # Calculate the number of cards given to Miguel
    given_to_miguel = total_given - (num_friends * cards_per_friend) - (sisters_num * sisters_cards)

    result = given_to_miguel
    return result

print(solution())