def solution():
    """When three friends sold their video games, Ryan, the first of the three friends, received $50 more than Jason from his sales. Jason received 30% more money than Zachary from selling his video games. If Zachary sold 40 games at $5 each, calculate the total amount of money the three friends received together from the sale of the video games."""
    zachary_sales = 40 * 5
    jason_sales = zachary_sales * 1.3
    ryan_sales = jason_sales + 50
    total_sales = zachary_sales + jason_sales + ryan_sales
    result = total_sales
    return result

print(solution())