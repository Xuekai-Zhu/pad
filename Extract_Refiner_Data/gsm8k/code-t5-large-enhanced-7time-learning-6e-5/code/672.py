def solution():
    
    # Define the initial investment amount
    initial_investment = 1200

    # Calculate the total amount invested by Dylan's investment
    dylan_investment = initial_investment * (2/5)

    # Calculate the remaining amount after Dylan's investment
    remaining_amount = initial_investment - dylan_investment

    # Calculate the amount invested by Frances's investment
    frances_investment = remaining_amount * (2/3)

    # Calculate the amount invested by Skyler's investment
    skyler_investment = remaining_amount - frances_investment

    # Display the amount invested by Skyler's investment
    result = skyler_investment
    return result

print(solution())