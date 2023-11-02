def solution():
    # Calculate the total earnings from selling samoas to the green house
    samoas_earnings = 3 * 4  # Three boxes of samoas sold for $4 each

    # Calculate the total earnings from selling thin mints to the green house
    thin_mints_earnings = 2 * 3.5  # Two boxes of thin mints sold for $3.50 each

    # Calculate the total earnings from selling fudge delights to the yellow house
    fudge_delights_earnings = 1 * 5  # One box of fudge delights sold for $5

    # Calculate the total earnings from selling sugar cookies to the brown house
    sugar_cookies_earnings = 9 * 2  # Nine boxes of sugar cookies sold for $2 each

    # Calculate the total earnings from all the sales
    total_earnings = samoas_earnings + thin_mints_earnings + fudge_delights_earnings + sugar_cookies_earnings
    result = total_earnings
    return result

print(solution())