def solution():
    """Kelly puts string cheeses in her kids lunches 5 days per week.  Her oldest wants 2 every day and her youngest will only eat 1.  The packages come with 30 string cheeses per pack.  How many packages of string cheese will Kelly need to fill her kids lunches for 4 weeks?"""
    # Define the number of string cheeses needed per week
    WEEKLY_NEED = 2 + 1  # 2 for oldest, 1 for youngest

    # Define the number of string cheeses needed per month
    MONTHLY_NEED = WEEKLY_NEED * 5 * 4  # 5 days per week, 4 weeks per month

    # Calculate the number of packages needed
    PACK_SIZE = 30
    packages_needed = MONTHLY_NEED / PACK_SIZE
    packages_needed = round(packages_needed + 0.5) # round up

    # Display the number of packages needed
    result = packages_needed
    return result

print(solution())