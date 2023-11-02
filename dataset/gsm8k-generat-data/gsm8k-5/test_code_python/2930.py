def solution():
    # Calculate the revenue from the group of 10 people
    group_10_revenue = (12 + 6) * 10  # $12 admission fee and $6 tour fee per person

    # Calculate the revenue from the group of 5 people
    group_5_revenue = 12 * 5  # $12 admission fee per person

    # Calculate the total revenue earned by the aqua park
    total_revenue = group_10_revenue + group_5_revenue
    result = total_revenue
    return result

print(solution())