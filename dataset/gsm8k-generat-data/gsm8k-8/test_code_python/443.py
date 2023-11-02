def solution():
    # Calculate the total earnings from selling 6 pairs of shoes
    shoes_earnings = 6 * 3

    # Calculate the total earnings from selling 18 shirts
    shirts_earnings = 18 * 2

    # Calculate the total earnings
    total_earnings = shoes_earnings + shirts_earnings

    # Divide the total earnings equally between Sab and Dane
    individual_earnings = total_earnings / 2

    result = individual_earnings
    return result

print(solution())