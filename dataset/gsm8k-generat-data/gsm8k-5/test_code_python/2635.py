def solution():
    old_apartment_cost = 1200  # John's old apartment cost $1200 per month
    new_apartment_cost = old_apartment_cost * 1.4  # The new apartment costs 40% more than the old one
    total_cost = new_apartment_cost / 3  # John and his two brothers split the cost of the new apartment

    # Calculate how much John saves per year by splitting the apartment
    saving_per_month = old_apartment_cost - total_cost
    saving_per_year = saving_per_month * 12
    result = saving_per_year
    return result

print(solution())