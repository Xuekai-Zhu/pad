def solution():
    """Duke was at a garage sale when he spotted DVDs on sale.  They were separated by price into 2 different boxes.  In the first box, he found 10 movies that he wanted.  These were $2.00 apiece.  The second box was marked $5 each and he found 5 movies he wanted.  What was the average price of each of the DVDs he bought?"""
    # Define the number of DVDs in each box and their respective prices
    BOX1_COUNT = 10
    BOX1_PRICE = 2.0
    BOX2_COUNT = 5
    BOX2_PRICE = 5.0

    # Calculate the total cost of the DVDs
    total_cost = (BOX1_COUNT * BOX1_PRICE) + (BOX2_COUNT * BOX2_PRICE)

    # Calculate the total number of DVDs
    total_count = BOX1_COUNT + BOX2_COUNT

    # Calculate the average price per DVD
    average_price = total_cost / total_count

    # Display the average price
    result = average_price
    return result

print(solution())