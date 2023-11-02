def solution():
    parker_throw = 16  # yards
    grant_throw = parker_throw * 1.25  # 25% farther than Parker
    kyle_throw = grant_throw * 2  # 2 times farther than Grant
    farther_than_parker = kyle_throw - parker_throw  # yards farther than Parker
    result = farther_than_parker
    return result

print(solution())