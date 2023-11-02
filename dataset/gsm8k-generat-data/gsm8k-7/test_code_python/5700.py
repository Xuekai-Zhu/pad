def solution():
    total_people = 200
    initial_snack_eaters = 100
    new_snack_eaters = 20
    new_outsiders = 10

    # Calculate the total number of snack eaters after new outsiders joined
    total_snack_eaters = initial_snack_eaters + new_snack_eaters + new_outsiders

    # Calculate the number of snack eaters who left after getting full
    first_wave_left = total_snack_eaters / 2

    # Calculate the number of snack eaters left after the first wave
    remaining_snack_eaters = total_snack_eaters - first_wave_left

    # Calculate the number of snack eaters who left after the second wave
    second_wave_left = 30
    remaining_snack_eaters -= second_wave_left

    # Calculate the final number of snack eaters who are left
    final_snack_eaters = remaining_snack_eaters / 2
    result = final_snack_eaters
    return result

print(solution())