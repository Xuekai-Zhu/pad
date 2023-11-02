def solution():
    # Define the total number of people served
    total_served = 25

    # Calculate the number of people who bought coffee
    coffee_buyers = int(total_served * 3/5)

    # Calculate the number of people who did not buy coffee
    non_coffee_buyers = total_served - coffee_buyers

    result = non_coffee_buyers
    return result

print(solution())