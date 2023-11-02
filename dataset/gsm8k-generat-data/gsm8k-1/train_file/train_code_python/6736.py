def solution():
    """Southton buries their time capsule 15 feet underground. Northton buries their time capsule 12 feet higher than 4 times the depth of the Southton time capsule. How deep is Northton's time capsule buried?"""
    southton_depth = 15
    northton_depth = 4 * southton_depth + 12
    result = northton_depth
    return result

print(solution())