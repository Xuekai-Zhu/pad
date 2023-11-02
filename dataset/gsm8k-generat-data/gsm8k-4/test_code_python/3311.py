def solution():
    """Porter is a painter who creates beautiful paintings of wild animals. Most recently, he painted a mural of a pack of wolves standing on a snowy-white mountainside underneath a full moon. He put the painting up for auction and it sold for $1000 less than five times more than he had made on his previous painting. If he received $44,000 for the sale of his most recent painting, how much, in dollars, did he make for selling his previous painting?"""
    
    recent_painting_sales = 44000

    # Calculate the minimum price of the most recent painting based on the previous painting
    # Let's assume the previous painting value as p
    five_times_previous_painting = 5 * p
    amount_less = 1000

    recent_painting_price = five_times_previous_painting - amount_less

    # Solving the expression for previous_painting
    previous_painting = (recent_painting_sales + five_times_previous_painting - amount_less)/6

    result = previous_painting
    return result

print(solution())