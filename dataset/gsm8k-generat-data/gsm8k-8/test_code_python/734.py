def solution():
    # Define the price and percentage of each type of apple
    sweet_price = 0.5
    sour_price = 0.1
    sweet_percent = 0.75
    sour_percent = 0.25

    # Calculate the total number of apples and the total earnings
    total_earnings = 40
    total_apples = total_earnings / ((sweet_price * sweet_percent) + (sour_price * sour_percent))

    result = total_apples
    return result

print(solution())