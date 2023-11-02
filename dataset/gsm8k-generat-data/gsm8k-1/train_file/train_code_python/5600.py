def solution():
    """Macy's is selling shirts that have been reduced to $6. This price is at 25% of the original price. What was the original price?"""
    reduced_price = 6
    percent_of_original = 25
    original_price = reduced_price / (percent_of_original / 100)
    result = original_price
    return result

print(solution())