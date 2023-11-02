def solution():
     time_to_chop_pepper = 3
     time_to_chop_onion = 4
     time_to_grate_cheese = 1
     time_to_assemble_and_cook_omelet = 5
     peppers_to_chop = 4
     onions_to_chop = 2
     omelets_to_make = 5
     total_time = (time_to_chop_pepper * peppers_to_chop) + (time_to_chop_onion * onions_to_chop) + (time_to_grate_cheese * omelets_to_make) + (time_to_assemble_and_cook_omelet * omelets_to_make)
     result = total_time
     return result

print(solution())