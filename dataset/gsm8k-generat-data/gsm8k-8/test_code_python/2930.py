def solution():
    # Calculate the total earnings from the group of 10
    group_of_10_admission = 10 * 12
    group_of_10_tour = 10 * 6
    group_of_10_earnings = group_of_10_admission + group_of_10_tour

    # Calculate the total earnings from the group of 5
    group_of_5_earnings = 5 * 12

    # Calculate the total earnings for the aqua park
    total_earnings = group_of_10_earnings + group_of_5_earnings
    result = total_earnings
    return result

print(solution())