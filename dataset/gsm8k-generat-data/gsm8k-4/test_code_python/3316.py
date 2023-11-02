def solution():
    """There were 50 candies left in a bowl after Shelly ate 20 candies the previous week. Her friend comes over, bringing twice as much candy as she originally had. Shelly adds this to the bowl and they decide to divide them equally. How much candy did her friend have after eating 10 of her candies?"""
    # Define the initial number of candies in the bowl
    initial_candies = 50

    # Define the number of candies Shelly ate
    shelly_candies = 20

    # Calculate the number of candies Shelly's friend brought
    friend_candies = initial_candies - shelly_candies

    # Double the number of candies Shelly's friend brought
    friend_candies *= 2

    # Add the friend's candies to the bowl
    total_candies = initial_candies + friend_candies

    # Divide the total candies equally between Shelly and her friend
    equal_candies = total_candies / 2

    # Subtract the candies that Shelly's friend ate
    friend_candies_left = friend_candies - 10

    # Return the final number of candies Shelly's friend had
    result = friend_candies_left
    return result

print(solution())