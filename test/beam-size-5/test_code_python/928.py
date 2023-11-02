def solution():
    num_friends = 4
    num_water_balloons_per_friend = 2
    num_water_balloons_given_by_mom = 1
    num_additional_balloons_per_person = 3

    # Calculate the total number of water balloons Maria gave to her friends
    total_water_balloons_given_by_friends = num_friends * num_water_balloons_per_friend

    # Calculate the total number of water balloons Maria gave to her mom
    total_water_balloons_given_by_mom = num_additional_balloons_per_person * num_water_balloons_given_by_mom

    # Calculate the total number of balloons the girls have
    total_balloons = total_water_balloons_given_by_friends + total_water_balloons_given_by_m

print(solution())