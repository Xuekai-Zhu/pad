def solution():
    num_pans = 2
    num_slices_per_pan = 16
    num_guests = 20  # Assuming there are 24 guests in total and 4 of them don't eat the brownies ala mode
    slices_consumed = num_slices_per_pan + (num_slices_per_pan * 0.75)
    num_brownie_slices_needed = (num_guests - 4) * 2
    num_tubs_of_ice_cream = num_brownie_slices_needed / 8
    result = num_tubs_of_ice_cream
    return result

print(solution())