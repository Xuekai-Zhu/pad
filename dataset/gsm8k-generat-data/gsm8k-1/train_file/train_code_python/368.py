def solution():
    """Monika went out for the day and spent some money. She went to the mall and spent $250. Then, she went to the movies and watched 3 movies back to back that each cost $24. Then she stopped by the farmer's market on her way home and got 20 bags of beans at $1.25/bag. How much money did Monika spend throughout her day?"""
    mall_spending = 250
    movie_cost = 24
    movies_watched = 3
    farmer_market_spending = 20 * 1.25
    total_spending = mall_spending + (movie_cost * movies_watched) + farmer_market_spending
    result = total_spending
    return result

print(solution())