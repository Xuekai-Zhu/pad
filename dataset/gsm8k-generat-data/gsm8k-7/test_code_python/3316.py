def solution():
    candies_left = 50
    candies_eaten_last_week = 20

    # Calculate the initial number of candies before Shelly ate 20
    initial_candies = candies_left + candies_eaten_last_week

    # Calculate the total number of candies after her friend brings twice as much
    total_candies = initial_candies + (2 * initial_candies)

    # Calculate the number of candies each person gets after they divide them equally
    num_people = 2
    candies_each = total_candies / num_people

    # Calculate how many candies Shelly's friend had left after eating 10
    friend_candies_left = candies_each - 10
    result = friend_candies_left
    return result

print(solution())