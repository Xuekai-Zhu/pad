def solution():
    """Sam bought a dozen boxes, each with 30 highlighter pens inside, for $10 each box. He rearranged five of these boxes into packages of six highlighters each and sold them for $3 per package. He sold the rest of the highlighters separately at the rate of three pens for $2. How much profit did he make in total, in dollars?"""
    # Define the initial cost of purchasing the boxes
    box_cost = 12 * 10

    # Calculate the number of highlighters in all the boxes
    total_highlighters = 12 * 30

    # Calculate the number of highlighters in the five boxes rearranged into packages
    packaged_highlighters = 5 * 6

    # Calculate the number of packaged highlighters sold
    packaged_highlighters_sold = packaged_highlighters // 6

    # Calculate the remaining number of highlighters sold separately
    remaining_highlighters_sold = total_highlighters - (packaged_highlighters_sold * 6)

    # Calculate the total earnings from selling the packaged highlighters
    packaged_earnings = packaged_highlighters_sold * 3

    # Calculate the total earnings from selling the remaining highlighters
    remaining_earnings = (remaining_highlighters_sold // 3) * 2

    # Calculate the total profit
    total_profit = packaged_earnings + remaining_earnings - box_cost

    # Display the result
    result = total_profit
    return result

print(solution())