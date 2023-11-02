def solution():
    members = 4  # John joins with 3 other members of his family
    join_fee = 4000  # The fee to join is $4000 per person
    monthly_cost = 1000  # The monthly cost is $1000 per person
    first_year_months = 12  # The first year lasts for 12 months

    # Calculate the total cost for one member for the first year
    one_member_cost = join_fee + (monthly_cost * first_year_months)

    # Calculate the total cost for all members for the first year
    total_cost = one_member_cost * members

    # Calculate the amount John pays for the first year (half the total cost)
    john_payment = total_cost / 2
    result = john_payment
    return result

print(solution())