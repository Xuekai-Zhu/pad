def solution():
    """Porter is a painter who creates beautiful paintings of wild animals. Most recently, he painted a mural of a pack of wolves standing on a snowy-white mountainside underneath a full moon. He put the painting up for auction and it sold for $1000 less than five times more than he had made on his previous painting. If he received $44,000 for the sale of his most recent painting, how much, in dollars, did he make for selling his previous painting?"""
    recent_sale = 44000
    previous_sale = (recent_sale + 1000) / 5
    result = previous_sale
    return result

print(solution())