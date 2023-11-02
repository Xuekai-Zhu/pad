def solution():
    """There were 50 candies left in a bowl after Shelly ate 20 candies the previous week. Her friend comes over, bringing twice as much candy as she originally had. Shelly adds this to the bowl and they decide to divide them equally. How much candy did her friend have after eating 10 of her candies?"""
    shelly_starting_candies = 20
    current_candies = 50 + shelly_starting_candies
    friend_starting_candies = current_candies / 3
    friend_candies_after_eating = friend_starting_candies - 10
    result = friend_candies_after_eating
    return result

print(solution())