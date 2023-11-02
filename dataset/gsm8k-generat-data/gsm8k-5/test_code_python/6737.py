def solution():
    southton_depth = 15  # Southton buried their time capsule 15 feet underground
    northton_depth = 4 * southton_depth + 12  # Northton buried their time capsule 12 feet higher than 4 times the depth of Southton's
    result = northton_depth
    return result

print(solution())