def solution():
    sweet_apple_price = 0.5
    sour_apple_price = 0.1
    total_earnings = 40
    sweet_apple_percentage = 0.75

    # Determine the ratio of sweet to sour apples
    sour_apple_percentage = 1 - sweet_apple_percentage

    # Determine the total number of apples
    total_apples = total_earnings / ((sweet_apple_price * sweet_apple_percentage) + (sour_apple_price * sour_apple_percentage))

    # Determine the number of sweet apples
    num_sweet_apples = total_apples * sweet_apple_percentage

    # Determine the number of sour apples
    num_sour_apples = total_apples * sour_apple_percentage

    result = total_apples
    return result

print(solution())