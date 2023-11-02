def solution():
    """Juan asked his neighbor, Herb, how much his house was worth. Herb answered that he paid $76,000 for the house. If Juan's house is 30% less expensive than Herb's, calculate the value of the two houses combined."""
    herb_house_price = 76000
    juan_house_price = herb_house_price * 0.7
    combined_price = herb_house_price + juan_house_price
    result = combined_price
    return result

print(solution())