def solution():
    num_masks_march = 3000
    doubling_factor = 2

    # Calculate the total mask production for each month
    num_masks_april = num_masks_march * doubling_factor
    num_masks_may = num_masks_april * doubling_factor
    num_masks_june = num_masks_may * doubling_factor
    num_masks_july = num_masks_june * doubling_factor

    # Calculate the total mask production for July
    total_masks_july = num_masks_march + num_masks_april + num_masks_may + num_masks_june + num_masks_july
    result = total_masks_july
    return result

print(solution())