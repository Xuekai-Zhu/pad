def solution():
    # Calculate the total number of apples and the number of sweet apples
    total_earnings = 40
    sweet_price = 0.5
    sour_price = 0.1
    sweet_percentage = 0.75
    total_apples = total_earnings / (sweet_price*sweet_percentage + sour_price*(1-sweet_percentage))
    sweet_apples = total_apples * sweet_percentage

    result = total_apples
    return result

print(solution())