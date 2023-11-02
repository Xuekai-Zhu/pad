def solution():
    winter_time = 40  # The duck takes 40 days to fly to the south during winter
    summer_time = 2 * winter_time  # It takes twice as much time to fly to the north during summer
    spring_time = 60  # It takes 60 days to travel to the East during spring

    # Calculate the total time the duck is flying during these seasons
    total_time = winter_time + summer_time + spring_time
    result = total_time
    return result

print(solution())