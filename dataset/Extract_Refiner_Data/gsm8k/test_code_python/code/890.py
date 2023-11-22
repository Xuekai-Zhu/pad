def solution():
    
    # Define the amount made from Joe's sales
    joe_sales = 6

    # Calculate the number of times she mowed Kamala's lawn
    kamala_weekly_mowers = 3 * joe_sales

    # Calculate the number of times she mowed Alba's lawn
    alba_weekly_mowers = 5 * joe_sales

    # Calculate the total amount made from mowing lawns
    total_mowing_amount = kamala_weekly_mowers + alba_weekly_mowers

    # Calculate the total amount made from sales
    total_sales = 80 - total_mowing_amount + joe_sales

    # Display the total amount made
    result = total_sales
    return result

print(solution())