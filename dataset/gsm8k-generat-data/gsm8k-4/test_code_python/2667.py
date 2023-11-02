def solution():
    """When three friends sold their video games, Ryan, the first of the three friends, received $50 more than Jason from his sales. Jason received 30% more money than Zachary from selling his video games. If Zachary sold 40 games at $5 each, calculate the total amount of money the three friends received together from the sale of the video games."""
    # Calculate the amount of money Zachary received from selling his games
    zachary_money = 40 * 5

    # Calculate the amount of money Jason received, which is 30% more than what Zachary received 
    jason_money = zachary_money * 1.3

    # Calculate the amount of money Ryan received, which is $50 more than what Jason received
    ryan_money = jason_money + 50

    # Calculate the total amount of money the three friends received together from the sale of the video games
    total_money = zachary_money + jason_money + ryan_money

    result = total_money
    return result

print(solution())