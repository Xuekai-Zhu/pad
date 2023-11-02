def solution():
    candies = 10  # Chenny has 10 pieces of candies
    candies_per_friend = 2  # Chenny wants to give each of her friends 2 candies
    extra_candies = 4  # Chenny needs to buy 4 more candies

    # Calculate the total number of friends Chenny has
    total_friends = (candies + extra_candies) / candies_per_friend
    result = total_friends
    return result

print(solution())