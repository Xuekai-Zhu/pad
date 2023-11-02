def solution():
    # Define initial variables
    initial_candies = 20
    remaining_candies = 50
    friend_candies = 2 * initial_candies
    total_candies = remaining_candies + friend_candies
    equal_division = total_candies / 2

    # Subtract 10 from the friend's candies
    friend_candies -= 10

    # Calculate how much candy is left for each person
    candy_per_person = (total_candies - 10) / 2
    result = friend_candies
    return result

print(solution())