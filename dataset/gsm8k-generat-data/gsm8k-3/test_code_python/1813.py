def solution():
    """Carrie harvested 200 tomatoes and 350 carrots on her farm. If she can sell a tomato for $1 and a carrot for $1.50, how much money can she make if she sells all of her tomatoes and carrots?"""
    # Define the selling price of tomatoes and carrots
    TOMATO_PRICE = 1
    CARROT_PRICE = 1.5

    # Calculate the total revenue from selling all the tomatoes and carrots
    total_revenue = (200 * TOMATO_PRICE) + (350 * CARROT_PRICE)

    # Display the total revenue
    result = total_revenue
    return result

print(solution())