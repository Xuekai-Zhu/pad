def solution():
    num_shoes = 6
    shoe_price = 3

    num_shirts = 18
    shirt_price = 2

    # Calculate the total earnings from selling shoes
    shoe_earnings = num_shoes * shoe_price

    # Calculate the total earnings from selling shirts
    shirt_earnings = num_shirts * shirt_price

    # Calculate the total earnings
    total_earnings = shoe_earnings + shirt_earnings

    # Calculate the earning per person if they divide their earnings equally
    individual_earnings = total_earnings / 2
    result = individual_earnings
    return result

print(solution())