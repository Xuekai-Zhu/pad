def solution():
    
    # Define the base price of each implant and the cost of the crown
    BASE_PRICE = 2000
    PORCELAIN_COST = 500

    # Define the number of implants and the cost of the porcelain
    NUM_EXPANDS = 2
    PORCELAIN_COST = PORCELAIN_COST

    # Define the total cost of the dental work
    total_cost = (BASE_PRICE * NUM_EXPANDS) + PORCELAIN_COST

    # Define the amount already put down a deposit
    deposit = 600

    # Define the hourly wage
    HOURLY_WAGE = 15

    # Calculate the number of hours George needs to work to pay for the dental work
    hours_work = total_cost / HOURLY_WAGE

    # Display the number of hours George needs to work
    result = hours_work
    return result

print(solution())