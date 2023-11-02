def solution():
    # Calculate the total number of candies in the bowl after Shelly's friend arrives
    total_candies = 50 + 2*20  # 50 candies left in the bowl after Shelly ate 20, her friend brings twice as much as she originally had
    remaining_candies = total_candies - 10  # Shelly's friend eats 10 candies
    equal_candies = remaining_candies / 2  # the candies are divided equally between Shelly and her friend
    result = equal_candies
    return result

print(solution())