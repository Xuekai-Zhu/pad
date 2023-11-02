def solution():
    # Calculate the number of pounds Calvin would have lost after one year
    pounds_lost = 8 * 12  # he loses 8 pounds every month for a year
    weight_after_one_year = 250 - pounds_lost  # subtract the pounds lost from his initial weight
    result = weight_after_one_year
    return result

print(solution())