def solution():
    amanda_start = 7
    amanda_first_gift = 3
    amanda_second_gift = amanda_first_gift * 4
    amanda_bought = 30

    # Calculate the total number of candy bars Amanda gave to her sister
    total_gifted = amanda_first_gift + amanda_second_gift

    # Calculate the total number of candy bars Amanda had after all the gifting and buying
    total_candy_bars = amanda_start - total_gifted + amanda_bought

    result = total_candy_bars
    return result

print(solution())