def solution():
    """For every loaf of bread that Ted buys, he needs an additional 2 packs of sandwich meat and 2 packs of sliced cheese to make 10 sandwiches.  The bread costs $4.00, the sandwich meat costs $5.00 per pack and the cheese costs $4.00 per pack.  He has a $1.00 off  coupon for one pack of cheese and an additional $1.00 coupon for one pack of meat.  How much does each sandwich cost?"""
    # Define the cost of each item
    BREAD_PRICE = 4.00
    MEAT_PRICE = 5.00
    CHEESE_PRICE = 4.00

    # Define the number of packs of meat and cheese needed per loaf of bread
    MEAT_PER_BREAD = 2
    CHEESE_PER_BREAD = 2

    # Define the number of sandwiches per loaf of bread
    SANDWICHES_PER_BREAD = 10

    # Define the coupons
    CHEESE_COUPON = 1.00
    MEAT_COUPON = 1.00

    # Calculate the total cost of the bread
    bread_cost = BREAD_PRICE

    # Calculate the total cost of the meat
    meat_cost = (MEAT_PRICE * MEAT_PER_BREAD * SANDWICHES_PER_BREAD) - MEAT_COUPON

    # Calculate the total cost of the cheese
    cheese_cost = (CHEESE_PRICE * CHEESE_PER_BREAD * SANDWICHES_PER_BREAD) - CHEESE_COUPON

    # Calculate the total cost of all the ingredients
    total_cost = bread_cost + meat_cost + cheese_cost

    # Calculate the cost per sandwich
    sandwiches_cost = total_cost / (SANDWICHES_PER_BREAD * MEAT_PER_BREAD)

    # Display the cost per sandwich
    result = sandwiches_cost
    return result

print(solution())