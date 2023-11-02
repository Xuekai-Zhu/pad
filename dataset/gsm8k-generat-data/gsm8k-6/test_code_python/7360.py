def solution():
    # Calculate the total number of golden apples Apollo needs to pay for the entire year
    first_half = 3 * 6   # Apollo paid 3 golden apples for the first 6 months
    second_half = 6 * 2   # For the second half of the year, Hephaestus demands twice as many golden apples as before
    total_apples = first_half + second_half 
    result = total_apples
    return result

print(solution())