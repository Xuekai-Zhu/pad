def solution():
    """There were 50 candies left in a bowl after Shelly ate 20 candies the previous week. Her friend comes over, bringing twice as much candy as she originally had. Shelly adds this to the bowl and they decide to divide them equally. How much candy did her friend have after eating 10 of her candies?"""
    candies_after_shelly = 50
    candies_before_shelly = candies_after_shelly + 20
    candies_before_friend = candies_before_shelly / 2
    candies_after_friend = candies_before_friend - 10
    result = candies_after_friend
    return result

print(solution())