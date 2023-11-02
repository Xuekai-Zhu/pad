def solution():
    num_towels_per_guest = 1
    num_towels_at_start = 300
    num_guests_first_hour = 50
    num_guests_second_hour = int(num_guests_first_hour * 1.2)
    num_guests_third_hour = int(num_guests_second_hour * 1.25)
    num_guests_fourth_hour = int(num_guests_third_hour * 1.33)
    total_num_guests = num_guests_first_hour + num_guests_second_hour + num_guests_third_hour + num_guests_fourth_hour

    # Calculate the total number of towels used
    total_num_towels_used = total_num_guests * num_towels_per_guest

    # Calculate the number of towels that need to be washed
    num_towels_to_wash = total_num_towels_used - num_towels_at_start
    result = num_towels_to_wash
    return result

print(solution())