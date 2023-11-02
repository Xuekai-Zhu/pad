def solution():
    # Calculate the initial number of dislikes
    dislikes = (3000 - 100) * 2/1  # 100 more than half as many as dislikes

    # Add the 1000 more dislikes
    dislikes += 1000

    result = dislikes
    return result

print(solution())