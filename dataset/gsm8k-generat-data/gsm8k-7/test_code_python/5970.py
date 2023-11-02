def solution():
    jared_popcorn = 90
    friend_popcorn = 60
    total_popcorn = jared_popcorn + (3 * friend_popcorn)
    popcorn_per_serving = 30
    
    # Calculate the total number of servings needed
    total_servings = total_popcorn / popcorn_per_serving
    
    result = total_servings
    return result

print(solution())