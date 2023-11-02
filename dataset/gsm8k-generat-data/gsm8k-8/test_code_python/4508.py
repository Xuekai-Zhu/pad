def solution():
    # Define the number of initial likes and calculate the number of initial dislikes
    initial_likes = 3000
    initial_dislikes = 100 + 0.5 * initial_likes

    # Calculate the total number of dislikes after 1000 more are added
    total_dislikes = initial_dislikes + 1000

    result = total_dislikes
    return result

print(solution())