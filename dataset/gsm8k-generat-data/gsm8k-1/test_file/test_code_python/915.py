def solution():
    """To raise money for their class fund, each of the 30 students from one class sold lollipops that cost $0.8 per lollypop. On average, each student sold 10 lollipops. If they bought the lollipops for $0.5 each, how much money was the class able to raise from the profit of selling lollipops?"""
    num_students = 30
    cost_per_lollipop = 0.5
    selling_price = 0.8
    num_lollipops_per_student = 10
    total_lollipops_sold = num_students * num_lollipops_per_student
    total_cost = total_lollipops_sold * cost_per_lollipop
    total_revenue = total_lollipops_sold * selling_price
    profit = total_revenue - total_cost
    result = profit
    return result

print(solution())