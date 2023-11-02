def solution():
    """A bag was originally priced at $500. A week after, the price was reduced by 5%. Since the bag was still not sold, 
    the selling price was reduced by 4% a month after. How much was the total reduction from the original selling price?"""
    original_price = 500
    first_reduction = original_price * 0.05
    first_price = original_price - first_reduction
    second_reduction = first_price * 0.04
    final_price = first_price - second_reduction
    total_reduction = original_price - final_price
    result = total_reduction
    
    return result

print(solution())