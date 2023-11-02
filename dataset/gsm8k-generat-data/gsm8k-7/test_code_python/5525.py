def solution():
    initial_bags = 20
    given_away = 4
    bought = 6

    # Calculate the total number of bags Abie has in the end
    total_bags = initial_bags - given_away + bought
    result = total_bags
    return result

print(solution())