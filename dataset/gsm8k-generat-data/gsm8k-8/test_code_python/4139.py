def solution():
    # Eric has 4 stars
    eric_stars = 4
    
    # Chad has twice as many as Eric
    chad_stars = eric_stars * 2
    
    # Jeff bought 2 stars from Chad
    chad_stars -= 2
    
    # Jeff now has 6 stars
    jeff_stars = 6
    
    # Calculate the total number of stars
    total_stars = eric_stars + chad_stars + jeff_stars
    result = total_stars
    return result

print(solution())