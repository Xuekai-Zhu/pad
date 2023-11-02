def solution():
    """A bag was originally priced at $500. A week after, the price was reduced by 5%. Since the bag was still not sold, the selling price was reduced by 4% a month after. How much was the total reduction from the original selling price?"""
    original_price = 500
    week_reduction = 0.05 * original_price
    week_price = original_price - week_reduction
    month_reduction = 0.04 * week_price
    final_price = week_price - month_reduction
    total_reduction = original_price - final_price
    result = total_reduction
    return result

print(solution())