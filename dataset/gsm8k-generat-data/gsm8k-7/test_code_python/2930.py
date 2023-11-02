def solution():
    admission_price = 12
    tour_price = 6

    # Calculate the total earnings from the group of 10 people
    group_10_earnings = (admission_price + tour_price) * 10

    # Calculate the total earnings from the group of 5 people
    group_5_earnings = admission_price * 5

    # Calculate the total earnings for the aqua park
    total_earnings = group_10_earnings + group_5_earnings
    result = total_earnings
    return result

print(solution())