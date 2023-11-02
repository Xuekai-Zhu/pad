def solution():
    """John joins a country club with 3 other members of his family.  The fee to join is $4000 per person.  There is also a monthly cost of $1000 per person.  John pays half the cost.  How much does John pay for the first year?"""
    # Define the number of family members
    num_members = 4

    # Calculate the total cost to join the country club
    join_cost = num_members * 4000

    # Calculate the monthly cost per person
    monthly_cost = num_members * 1000

    # Calculate the total annual cost
    annual_cost = join_cost + (monthly_cost * 12)

    # Calculate the amount that John pays
    john_cost = annual_cost / 2

    # Return the result
    result = john_cost
    return result

print(solution())