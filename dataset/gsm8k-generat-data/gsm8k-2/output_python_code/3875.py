def solution():
    """On Thursday the Meat Market sold 210kg of ground beef. On Friday they sold twice that amount. On Saturday they only sold 130kg. On Sunday they sold half of what they sold Saturday. If they originally planned to sell only 500kg, how much meat did they sell beyond their original plans?"""
    thursday_sales = 210
    friday_sales = 2 * thursday_sales
    saturday_sales = 130
    sunday_sales = 0.5 * saturday_sales
    total_sales = thursday_sales + friday_sales + saturday_sales + sunday_sales
    meat_sold_beyond_plans = total_sales - 500
    result = meat_sold_beyond_plans
    return result

print(solution())