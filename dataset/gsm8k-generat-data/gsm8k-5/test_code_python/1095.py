def solution():
    # Ignatius has 4 bicycles, which have 2 tires each, for a total of 8 tires
    ignatius_tires = 8

    # The friend's cycles have 3 times as many tires as Ignatius's bikes, so the total number of tires is 3 times 8, or 24
    friend_tires = 24

    # The friend has one unicycle, which has 1 tire, and one tricycle, which has 3 tires, so the total number of tires from bikes is 24 - 1 - 3 = 20
    bike_tires = 20

    # Each bike has 2 tires, so the friend must have 10 bikes
    num_bikes = bike_tires / 2

    result = num_bikes
    return result

print(solution())