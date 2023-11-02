def solution():
    """Mike bought a DVD of his favorite movie. He paid $5 for it at the store. A friend of Mike's, Steve, saw this and also decided to buy a DVD of the movie, but it was already sold out. He needed to order it online, which cost him twice as much. And in addition, he needed to pay the shipping costs which were 80% of the price of the film he ordered. How much did Steve pay to get the DVD in total?"""
    # Define the cost of the DVD
    dvd_cost = 5

    # Calculate the cost of the DVD for Steve
    steve_dvd_cost = dvd_cost * 2

    # Calculate the shipping cost for Steve
    shipping_cost = steve_dvd_cost * 0.8

    # Calculate the total cost for Steve
    total_cost = steve_dvd_cost + shipping_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())