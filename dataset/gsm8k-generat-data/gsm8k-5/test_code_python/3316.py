def solution():
    candies_initial = 50 + 20  # Shelly ate 20 candies, so there were initially 50 + 20 candies in the bowl
    candies_friend_initial = 2 * candies_initial  # Shelly's friend brought twice as much candy as she had

    # Calculate the total amount of candies after Shelly's friend brings her candies
    candies_total = candies_initial + candies_friend_initial

    # Divide the candies equally between Shelly and her friend
    candies_each = candies_total / 2

    # Calculate how much candy Shelly's friend has left after eating 10 candies
    candies_friend_left = candies_friend_initial - (candies_each - 10)
    result = candies_friend_left
    return result

print(solution())