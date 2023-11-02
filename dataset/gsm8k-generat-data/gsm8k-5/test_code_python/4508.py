def solution():
    likes = 3000
    half_dislikes = (likes / 2) + 100  # Half as many dislikes + 100
    dislikes = half_dislikes + 1000  # Add 1000 more dislikes

    result = dislikes
    return result

print(solution())