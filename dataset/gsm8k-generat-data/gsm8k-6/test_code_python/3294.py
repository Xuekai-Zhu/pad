def solution():
    # Calculate the number of cows on the ranch after 1 year
    cows_after_1_year = 200 + (1/2)*200  # half of the existing cows are born as calves

    # Calculate the number of cows on the ranch after 2 years
    cows_after_2_years = cows_after_1_year + (1/2)*cows_after_1_year  

    result = cows_after_2_years
    return result

print(solution())