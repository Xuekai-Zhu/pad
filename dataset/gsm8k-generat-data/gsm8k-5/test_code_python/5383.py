def solution():
    bundles_of_wood_in_the_morning = 4  # A wood stove burns 4 bundles of wood in the morning
    bundles_of_wood_at_the_start_of_the_day = 10  # There were 10 bundles of wood at the start of the day
    bundles_of_wood_at_the_end_of_the_day = 3  # There were 3 bundles of wood at the end of the day

    # Calculate the total number of bundles of wood burned during the day
    total_bundles_of_wood_burned = bundles_of_wood_at_the_start_of_the_day - bundles_of_wood_at_the_end_of_the_day
    bundles_of_wood_burned_in_the_afternoon = total_bundles_of_wood_burned - bundles_of_wood_in_the_morning
    result = bundles_of_wood_burned_in_the_afternoon
    return result

print(solution())