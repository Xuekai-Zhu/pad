def solution():
    # Calculate the total amount of money they need to earn
    total_money = 60  # the cost of the video game
    money_earned_per_ice_cream = 5
    money_needed = total_money - 0  # assume they have no money yet

    # Calculate the number of ice creams they need to sell
    number_of_ice_creams = money_needed / money_earned_per_ice_cream
    
    # Round up to the nearest integer
    number_of_ice_creams = int(number_of_ice_creams) + 1 if number_of_ice_creams % 1 != 0 else int(number_of_ice_creams)
    
    result = number_of_ice_creams
    return result

print(solution())