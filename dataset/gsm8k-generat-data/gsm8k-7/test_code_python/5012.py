def solution():
    num_button_up_shirts = 3
    num_sweater_vests = 2 * num_button_up_shirts

    # Calculate the total number of outfit combinations
    total_outfits = num_sweater_vests * num_button_up_shirts

    result = total_outfits
    return result

print(solution())