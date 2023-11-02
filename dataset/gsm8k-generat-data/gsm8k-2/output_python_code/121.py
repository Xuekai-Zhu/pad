def solution():
    """Stella and Twinkle are filling up a truck with a capacity of 6000 stone blocks at the rate of 250 blocks per hour per person.
    They work for four hours and are then joined by 6 other people who also work at the same rate. How many hours did filling the truck take?"""

    capacity = 6000
    rate_per_person_per_hour = 250
    initial_workers = 2
    hours_with_initial_workers = 4
    additional_workers = 6

    # Work done by Stella and Twinkle in the first 4 hours
    blocks_filled_in_four_hours = initial_workers * rate_per_person_per_hour * hours_with_initial_workers

    # Work done by all 8 workers
    total_rate = (initial_workers + additional_workers) * rate_per_person_per_hour

    # Remaining blocks to be filled
    blocks_left = capacity - blocks_filled_in_four_hours

    # Time taken to fill remaining blocks
    time_taken_to_fill_remaining_blocks = blocks_left / total_rate

    # Total time taken
    total_time_taken = hours_with_initial_workers + time_taken_to_fill_remaining_blocks

    result = total_time_taken
    return result

print(solution())