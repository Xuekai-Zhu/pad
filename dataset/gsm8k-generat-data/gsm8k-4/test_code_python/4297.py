def solution():
    """Duke was at a garage sale when he spotted DVDs on sale. They were separated by price into 2 different boxes. In the first box, he found 10 movies that he wanted. These were $2.00 apiece. The second box was marked $5 each and he found 5 movies he wanted. What was the average price of each of the DVDs he bought?"""
    # Define the number of movies and the prices
    num_movies = 15
    price_box1 = 2
    num_box1 = 10
    price_box2 = 5
    num_box2 = 5

    # Calculate the total cost of the movies
    total_cost = (price_box1 * num_box1) + (price_box2 * num_box2)

    # Calculate the average price per movie
    avg_price = total_cost / num_movies

    # Return the result
    result = avg_price
    return result

print(solution())