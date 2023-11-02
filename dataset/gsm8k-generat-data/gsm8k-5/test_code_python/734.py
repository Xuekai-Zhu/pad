def solution():
    sweet_apple_proportion = 0.75  # 75% of apples are sweet
    sour_apple_proportion = 0.25  # The remaining 25% are sour
    sweet_apple_price = 0.5  # Sweet apples sell for $0.5 each
    sour_apple_price = 0.1  # Sour apples sell for $0.1 each
    total_earnings = 40  # Chang's Garden earns $40 selling apples

    # Calculate the total number of apples
    total_apples = total_earnings / ((sweet_apple_proportion * sweet_apple_price) + (sour_apple_proportion * sour_apple_price))

    result = total_apples
    return result

print(solution())