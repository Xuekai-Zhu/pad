def solution():
    # Calculate the number of ducks remaining after each night
    ducks_left = 320 * (3/4) * (5/6) * (0.7)  # 1/4 eaten by fox, 1/6 fly away, 30% stolen
    result = ducks_left
    return result

print(solution())