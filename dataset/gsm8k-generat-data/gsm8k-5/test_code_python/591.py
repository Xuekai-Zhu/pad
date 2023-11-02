def solution():
    pounds_of_cherries = 3  # Veronica needs 3 pounds of pitted cherries
    cherries_per_pound = 80  # There are 80 single cherries in one pound of cherries
    cherries_total = pounds_of_cherries * cherries_per_pound  # The total number of cherries needed

    cherries_per_10_min = 20  # Veronica can pit 20 cherries in 10 minutes
    minutes_per_hour = 60  # There are 60 minutes in one hour

    # Calculate the total time needed to pit all the cherries
    total_time_min = (cherries_total / cherries_per_10_min) * 10
    total_time_hrs = total_time_min / minutes_per_hour

    result = total_time_hrs
    return result

print(solution())