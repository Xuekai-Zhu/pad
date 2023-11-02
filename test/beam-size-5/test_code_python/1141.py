def solution():
    sunflower_price = 2
    bouquet_price = 8
    daily_earnings = 26
    daily_earnings = 56
    num_days = 3

    # Calculate the total earnings from selling sunflowers
    total_sunflower_earnings = daily_earnings * num_days

    # Calculate the total earnings from selling bouquet
    total_bouquet_earnings = daily_earnings * num_days

    # Calculate the total number of sunflowers sold
    total_sunflowers_sold = total_sunflower_earnings / sunflower_price
    result = total_sunflowers_sold
    return result

print(solution())