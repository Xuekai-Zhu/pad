def solution():
    """Maya's organization hosted a weekly farmers' market to raise money for the church choir. They sold broccolis, carrots, spinach, and cauliflowers. After adding together all of their earnings, Maya found out that they had made $380. The organization made $57 from broccoli and the sales of the carrots are twice as much as the sales of broccoli. Then, their sales for the spinach is $16 more than half of the sales of carrots. How much did they make from cauliflower sales?"""
    total_sales = 380
    broccoli_sales = 57
    carrot_sales = 2 * broccoli_sales
    spinach_sales = (carrot_sales / 2) + 16
    cauliflower_sales = total_sales - broccoli_sales - carrot_sales - spinach_sales
    result = cauliflower_sales
    return result

print(solution())