def solution():
    # Calculate the amount saved by Martha each day
    amount_saved = 12/2  # Martha saves half of her daily allowance

    # Calculate the total amount saved in the first week
    total_saved = 6 * amount_saved + (1/4) * amount_saved  # Martha missed one day and saved only a quarter of her allowance
    result = total_saved
    return result

print(solution())