def solution():
    """Porter painted a mural that sold for $1000 less than five times more than he had made on his previous painting. If he received $44,000 for the sale of his most recent painting, how much did he make for selling his previous painting?"""
    
    recent_sale = 44000
    previous_sale = (recent_sale + 1000) / 5
    result = previous_sale
    
    return result

print(solution())