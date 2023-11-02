def solution():
    """John joins a country club with 3 other members of his family.  The fee to join is $4000 per person.  There is also a monthly cost of $1000 per person.  John pays half the cost.  How much does John pay for the first year?"""
    # Define the cost to join and the monthly cost per person
    JOIN_COST = 4000
    MONTHLY_COST = 1000

    # Define the number of members in John's family, including himself
    num_members = 4

    # Calculate the total cost for all members to join
    total_join_cost = JOIN_COST * num_members

    # Calculate the total cost for one year of monthly fees
    yearly_monthly_cost = MONTHLY_COST * num_members * 12

    # Calculate the total cost for John to pay
    john_payment = (total_join_cost + yearly_monthly_cost) / 2

    # Display John's payment for the first year
    result = john_payment
    return result

print(solution())