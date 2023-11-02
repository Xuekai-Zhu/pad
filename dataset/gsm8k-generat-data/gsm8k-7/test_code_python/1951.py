def solution():
    initial_chips = 100
    eaten_on_first_day = 10
    eaten_per_day = 10

    # Calculate the total number of chips Marnie eats before finishing the bag
    total_eaten = 5 + 5 + eaten_on_first_day + (eaten_per_day * (initial_chips - 10))

    # Calculate the number of days it takes Marnie to finish the bag
    days_to_finish = (initial_chips - 10) / eaten_per_day + 2

    result = days_to_finish
    return result

print(solution())