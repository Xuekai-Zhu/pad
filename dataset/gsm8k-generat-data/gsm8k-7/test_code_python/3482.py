def solution():
    num_cotton_candies = 50
    num_given_away = 5*2
    num_eaten = 12

    # Calculate the remaining cotton candies after giving some away and eating some
    num_remaining = (num_cotton_candies - num_given_away - num_eaten) * 3 / 4
    result = num_remaining
    return result

print(solution())