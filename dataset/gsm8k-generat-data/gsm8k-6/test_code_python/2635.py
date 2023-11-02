def solution():
    # Calculate the cost of John's old apartment
    old_rent = 1200  # $1200 per month
    old_rent_yearly = old_rent * 12  # yearly cost of John's old apartment

    # Calculate the cost of the new apartment
    new_rent = old_rent * 1.4  # new apartment is 40% more expensive than John's old apartment
    total_rent = new_rent * 3  # John and his two brothers split the cost

    # Calculate John's savings
    john_share = new_rent / 3  # John pays 1/3 of the new rent
    john_savings = old_rent - john_share
    yearly_savings = john_savings * 12

    result = yearly_savings
    return result

print(solution())