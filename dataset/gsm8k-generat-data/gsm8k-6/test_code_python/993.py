def solution():
    # Calculate the total number of cards given away
    total_given_away = 130 - 15  # Rick kept 15 cards
    total_given_to_friends = 8 * 12  # 8 friends got 12 cards each
    total_given_to_sisters = 2 * 3  # 2 sisters got 3 cards each
    total_given_to_others = total_given_away - total_given_to_friends - total_given_to_sisters  # Miguel got the rest
    
    result = total_given_to_others
    return result

print(solution())