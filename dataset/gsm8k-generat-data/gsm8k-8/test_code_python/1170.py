def solution():
    # Calculate the total amount of time he spent stopped at red lights
    red_light_time = 4 * 3

    # Calculate the total time spent due to construction
    construction_time = 10

    # Calculate the total time he spent on the road
    travel_time = 30 + red_light_time + construction_time

    # Calculate the time he left his house
    leave_time = 7 * 60 + 15

    # Calculate the time he will arrive at school
    arrive_time = leave_time + travel_time

    # Calculate how many minutes late he will be
    late_time = arrive_time - 8 * 60

    result = late_time

    return result

print(solution())