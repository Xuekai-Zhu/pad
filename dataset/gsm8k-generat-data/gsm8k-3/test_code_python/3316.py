def solution():
    """There were 50 candies left in a bowl after Shelly ate 20 candies the previous week. Her friend comes over, bringing twice as much candy as she originally had. Shelly adds this to the bowl and they decide to divide them equally. How much candy did her friend have after eating 10 of her candies?"""
    # Calculate the initial number of candies before Shelly's friend arrived
    initial_candies = 50 + 20  # Shelly ate 20 candies the previous week

    # Calculate the number of candies that Shelly's friend brought
    friend_candies = 2 * initial_candies

    # Calculate the total number of candies after Shelly's friend arrived
    total_candies = initial_candies + friend_candies

    # Calculate the number of candies each person gets after dividing them equally
    each_person_candies = total_candies // 2  # // is used for integer division

    # Calculate the number of candies Shelly's friend has after eating 10 of them
    friend_candies_left = each_person_candies - 10

    # Display the number of candies Shelly's friend has left
    result = friend_candies_left
    return result

print(solution())