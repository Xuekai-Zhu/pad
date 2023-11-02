def solution():
    """Monika went out for the day and spent some money. She went to the mall and spent $250. Then, she went to the movies and watched 3 movies back to back that each cost $24. Then she stopped by the farmer's market on her way home and got 20 bags of beans at $1.25/bag. How much money did Monika spend throughout her day?"""
    # Define the cost of each activity
    MALL_COST = 250
    MOVIE_COST = 24
    BEAN_COST = 1.25

    # Define the number of movies watched
    num_movies = 3

    # Calculate the total cost of the movies
    movie_cost = num_movies * MOVIE_COST

    # Calculate the total cost of the beans
    bean_cost = 20 * BEAN_COST

    # Calculate the total cost of Monika's day
    total_cost = MALL_COST + movie_cost + bean_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())