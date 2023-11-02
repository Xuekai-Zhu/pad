def solution():
    # Calculate the number of people that can ride the roller coaster in one run
    people_per_run = 7*2  # There are 7 cars, each car seats 2 people

    # Calculate the number of runs needed to give everyone in line a turn
    runs_needed = 84 // people_per_run  # Floor division ensures all people get a turn
    if 84 % people_per_run != 0:
        runs_needed += 1  # If there are remaining people, add another run

    result = runs_needed
    return result

print(solution())