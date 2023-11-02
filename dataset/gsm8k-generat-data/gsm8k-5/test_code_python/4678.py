def solution():
    # Calculate the revenue from the first showing
    revenue_first_show = 200 * 25  # 200 people buy tickets at $25 per ticket

    # Calculate the number of people at the second showing and the revenue from that showing
    second_show_people = 3 * 200  # Three times as many people show up at the second showing
    revenue_second_show = second_show_people * 25

    # Calculate the total revenue from both shows
    total_revenue = revenue_first_show + revenue_second_show
    result = total_revenue
    return result

print(solution())