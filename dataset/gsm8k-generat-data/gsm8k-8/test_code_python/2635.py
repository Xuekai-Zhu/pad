def solution():
    # Calculate the cost of John's old apartment
    old_apartment_cost = 1200

    # Calculate the cost of the new apartment
    new_apartment_cost = old_apartment_cost * 1.4

    # Calculate John's share of the new apartment
    john_share = new_apartment_cost / 3

    # Calculate how much John saves per month by splitting the apartment
    savings_per_month = old_apartment_cost - john_share

    # Calculate how much John saves per year by splitting the apartment
    savings_per_year = savings_per_month * 12

    result = savings_per_year
    return result

print(solution())