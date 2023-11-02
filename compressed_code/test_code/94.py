def solution():
    

    capacity = 6000
    rate_per_person_per_hour = 250
    initial_workers = 2
    hours_with_initial_workers = 4
    additional_workers = 6

    
    blocks_filled_in_four_hours = initial_workers * rate_per_person_per_hour * hours_with_initial_workers

    
    total_rate = (initial_workers + additional_workers) * rate_per_person_per_hour

    
    blocks_left = capacity - blocks_filled_in_four_hours

    
    time_taken_to_fill_remaining_blocks = blocks_left / total_rate

    
    total_time_taken = hours_with_initial_workers + time_taken_to_fill_remaining_blocks

    result = total_time_taken
    return result

print(solution())