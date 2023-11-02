def solution():
    # Calculate the number of puppies John gives away
    given_puppies = 8 // 2 

    # Calculate the number of puppies John keeps
    remaining_puppies = 8 - given_puppies - 1

    # Calculate the total profit John makes
    total_profit = remaining_puppies * 600 - 300

    result = total_profit
    return result

print(solution())