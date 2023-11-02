def solution():
    jar_capacity = 160
    num_jars = 5
    cost_of_bike = 180

    # Calculate the total number of quarters Jenn has
    total_quarters = jar_capacity * num_jars

    # Calculate the total value of quarters Jenn has
    worth_of_quarters = total_quarters * 0.25

    # Calculate how much money Jenn will have left after buying the bike
    left_over_money = worth_of_quarters - cost_of_bike
    result = left_over_money
    return result

print(solution())