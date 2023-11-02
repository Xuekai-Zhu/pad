def solution():
    num_family_members = 4
    join_fee = 4000
    monthly_cost = 1000
    num_months = 12

    # Calculate the total cost for one family member for one year
    member_total_cost = join_fee + (monthly_cost * num_months)

    # Calculate the total cost for the whole family for one year
    family_total_cost = member_total_cost * num_family_members

    # Calculate how much John pays for the first year (half the total cost)
    john_payment = family_total_cost / 2
    result = john_payment
    return result

print(solution())