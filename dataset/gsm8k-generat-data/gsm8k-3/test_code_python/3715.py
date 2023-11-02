def solution():
    """Sam bought a dozen boxes, each with 30 highlighter pens inside, for $10 each box. He rearranged five of these boxes into packages of six highlighters each and sold them for $3 per package. He sold the rest of the highlighters separately at the rate of three pens for $2. How much profit did he make in total, in dollars?"""
    # Define the number of boxes and pens per box
    BOXES = 12
    PENS_PER_BOX = 30

    # Define the cost and selling price of each box
    BOX_COST = 10
    BOX_SELLING_PRICE = 0 # initialize variable
    # Calculate the selling price of each box as the cost per pen
    # divided by the number of pens per box
    PEN_COST = BOX_COST / (BOXES * PENS_PER_BOX)
    BOX_SELLING_PRICE = PEN_COST * 6 * 5 / 3

    # Define the cost and selling price of each pen
    PEN_COST = BOX_COST / (BOXES * PENS_PER_BOX)
    PEN_SELLING_PRICE = 2 / 3

    # Calculate the profit from selling the boxes
    box_profit = (BOX_SELLING_PRICE - PEN_COST) * 6 * 5

    # Calculate the profit from selling the loose pens
    pen_profit = (PEN_SELLING_PRICE - PEN_COST) * (BOXES * PENS_PER_BOX - 6 * 5)

    # Calculate the total profit
    total_profit = box_profit + pen_profit

    # Display the total profit
    result = total_profit
    return result

print(solution())