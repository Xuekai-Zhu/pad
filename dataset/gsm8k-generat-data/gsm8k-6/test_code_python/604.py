def solution():
    # Calculate the total number of presents that Santana needs to buy in the first half of the year
    presents_first_half = 7*2  # 7 brothers and 2 presents for each

    # Calculate the total number of presents that Santana needs to buy in the second half of the year
    presents_second_half = 3*2 + 1*2 + 2*2  # 3 brothers in March, 1 brother in October, 2 brothers in December and 2 presents for each

    # Calculate the difference between the two
    diff_presents = presents_second_half - presents_first_half
    result = diff_presents
    return result

print(solution())