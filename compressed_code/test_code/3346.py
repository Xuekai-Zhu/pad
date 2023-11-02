def solution():
    
    box1_movies = 10
    box1_price = 2
    box2_movies = 5
    box2_price = 5
    total_price = (box1_movies * box1_price) + (box2_movies * box2_price)
    avg_price = total_price / (box1_movies + box2_movies)
    result = avg_price
    return result

print(solution())