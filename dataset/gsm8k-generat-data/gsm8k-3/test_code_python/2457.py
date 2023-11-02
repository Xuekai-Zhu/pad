def solution():
    """A colony of bees can contain up to 80000 individuals. In winter they are more exposed to death, and if the winter is really cold the bees can begin to die slowly. If the colony starts to lose 1200 bees per day, how many days will pass until the number of bees in the colony reaches a fourth of its initial number?"""
    # Define the initial number of bees in the colony
    initial_count = 80000

    # Calculate the number of bees in the colony after a fourth have died
    final_count = initial_count / 4

    # Calculate the number of bees lost each day
    lost_per_day = 1200

    # Calculate the number of days until the final count is reached
    days_to_reach_final_count = (initial_count - final_count) / lost_per_day

    # Display the number of days
    result = days_to_reach_final_count
    return result

print(solution())