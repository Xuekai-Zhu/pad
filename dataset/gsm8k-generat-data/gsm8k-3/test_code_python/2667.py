def solution():
    """When three friends sold their video games, Ryan, the first of the three friends, received $50 more than Jason from his sales.
    Jason received 30% more money than Zachary from selling his video games. If Zachary sold 40 games at $5 each, calculate the total amount of money 
    the three friends received together from the sale of the video games."""
    
    # Calculate how much money Zachary made from selling his games
    zachary_money = 40 * 5
    
    # Calculate how much money Jason made from selling his games
    jason_money = zachary_money * 1.3
    
    # Calculate how much money Ryan made from selling his games
    ryan_money = jason_money + 50
    
    # Calculate the total amount of money the three friends received
    total_money = zachary_money + jason_money + ryan_money
    
    # Display the total amount of money
    result = total_money
    return result

print(solution())