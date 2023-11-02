def solution():
    """Duke was at a garage sale when he spotted DVDs on sale. They were separated by price into 2 different boxes. In the first box, he found 10 movies that he wanted. These were $2.00 apiece. The second box was marked $5 each and he found 5 movies he wanted. What was the average price of each of the DVDs he bought?"""
    box1_movies = 10
    box1_price = 2
    box2_movies = 5
    box2_price = 5
    total_price = (box1_movies * box1_price) + (box2_movies * box2_price)
    avg_price = total_price / (box1_movies + box2_movies)
    result = avg_price
    return result

print(solution())