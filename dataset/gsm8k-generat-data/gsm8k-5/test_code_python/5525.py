def solution():
    bags_of_chips = 20  # Abie had 20 bags of chips
    bags_given_away = 4  # Abie gave away 4 bags of chips
    bags_bought = 6  # Abie bought 6 bags of chips

    # Calculate the total number of bags of chips Abie has in the end
    total_bags = bags_of_chips - bags_given_away + bags_bought
    result = total_bags
    return result

print(solution())