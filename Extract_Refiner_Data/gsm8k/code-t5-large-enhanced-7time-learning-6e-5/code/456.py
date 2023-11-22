def solution():
    
    # Define the prices of aluminum and plastic bottles
    ALUM_PRICE = 2
    BOTTLE_PRICE = 3

    # Define the number of aluminum and plastic bottles purchased per week
    aluminum_cans = 3
    water_bottles = 5

    # Calculate the total earnings per week
    total_earnings = (aluminum_cans * ALUM_PRICE) + (water_bottles * BOTTLE_PRICE)

    # Calculate the total earnings per four-week month
    total_earnings_4_week_month = total_earnings * 4

    # Display the total earnings in a four-week month
    result = total_earnings_4_week_month
    return result

print(solution())