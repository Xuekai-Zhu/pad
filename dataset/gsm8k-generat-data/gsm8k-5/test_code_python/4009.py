def solution():
    num_cards = 365  # Jim had 365 trading cards
    num_cards_per_set = 13  # There are 13 trading cards in one set

    # Calculate the number of cards given away to Jim's brother
    num_sets_brother = 8
    num_cards_brother = num_sets_brother * num_cards_per_set

    # Calculate the number of cards given away to Jim's sister
    num_sets_sister = 5
    num_cards_sister = num_sets_sister * num_cards_per_set

    # Calculate the number of cards given away to Jim's friend
    num_sets_friend = 2
    num_cards_friend = num_sets_friend * num_cards_per_set

    # Calculate the total number of cards given away
    num_cards_given_away = num_cards_brother + num_cards_sister + num_cards_friend
    result = num_cards_given_away
    return result

print(solution())