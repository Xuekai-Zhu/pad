def solution():
    num_students = 30
    cost_per_lollypop = 0.8
    num_lollipops_per_student = 10
    selling_price_per_lollipop = 0.5

    # Calculate the total revenue from selling lollipops
    total_revenue = num_students * num_lollipops_per_student * selling_price_per_lollipop

    # Calculate the profit from selling lollipops
    profit = total_revenue - total_cost
    result = profit
    return result

print(solution())