def solution():
    """A gym charges its members $18 twice a month.  If it has 300 members how much does it make a month?"""
    # Define the price per visit and the number of members
    PRICE_PER_VISIT = 18
    NUM_MEMBERS = 300

    # Calculate the total revenue per month
    revenue = PRICE_PER_VISIT * 2 * NUM_MEMBERS

    # Display the total revenue
    result = revenue
    return result

print(solution())