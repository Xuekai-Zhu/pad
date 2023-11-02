def solution():
    # Define the initial number of racers
    start_racers = 100

    # Calculate the number of racers remaining after the first segment
    remaining_racers1 = start_racers - 10

    # Calculate the number of racers remaining after the second segment
    remaining_racers2 = remaining_racers1 - (1/3 * remaining_racers1)

    # Calculate the number of racers remaining before the last leg of the race
    remaining_racers3 = remaining_racers2 / 2

    # Calculate the final number of racers running in the last section
    final_racers = remaining_racers3

    result = final_racers
    return result

print(solution())