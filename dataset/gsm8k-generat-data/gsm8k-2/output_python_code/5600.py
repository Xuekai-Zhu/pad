def solution():
    """Macy's is selling shirts that have been reduced to $6. This price is at 25% of the original price. What was the original price?"""
    reduced_price = 6
    percentage_of_original_price = 25
    original_price = (100 / percentage_of_original_price) * reduced_price
    result = original_price
    return result

print(solution())