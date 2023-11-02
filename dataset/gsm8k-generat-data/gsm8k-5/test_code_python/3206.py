def solution():
    computers_per_day = 1500  # The factory produces 1500 computers per day
    price_per_computer = 150  # They sell each computer for $150
    days_per_week = 7  # There are 7 days in a week

    # Calculate the total number of computers produced in a week
    total_computers = computers_per_day * days_per_week

    # Calculate the total revenue earned by the company in a week
    total_revenue = total_computers * price_per_computer
    result = total_revenue
    return result

print(solution())