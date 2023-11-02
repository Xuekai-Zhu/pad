def solution():
    buttered_popcorn = 12
    caramel_popcorn = 10
    buttered_popcorn_taken = 3
    caramel_popcorn_taken = 1
    buttered_popcorn_left = buttered_popcorn - buttered_popcorn_taken
    caramel_popcorn_left = caramel_popcorn - caramel_popcorn_taken
    total_popcorn_left = buttered_popcorn_left + caramel_popcorn_left
    result = total_popcorn_left
    return result

print(solution())