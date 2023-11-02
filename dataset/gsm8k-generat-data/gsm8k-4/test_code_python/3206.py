def solution():
    """A computer factory produces 1500 computers per day. They sell each computer for $150. If they sold 1 week's worth of production, how much money will the company earn?"""
    # Define the number of days in a week and the number of computers produced per day
    DAYS_PER_WEEK = 7
    COMPUTERS_PER_DAY = 1500

    # Calculate the total number of computers produced in a week
    total_computers = COMPUTERS_PER_DAY * DAYS_PER_WEEK

    # Calculate the total revenue from selling all the computers
    total_revenue = total_computers * 150

    # Return the result
    result = total_revenue
    return result

print(solution())