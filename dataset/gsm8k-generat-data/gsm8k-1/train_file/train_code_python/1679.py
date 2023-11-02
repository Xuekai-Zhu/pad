def solution():
    """There were 349 pieces of candy in a bowl. Talitha took 108 pieces and Solomon took 153 pieces. How many pieces of candy remain in the bowl?"""
    initial_candy = 349
    candy_taken = 108 + 153
    remaining_candy = initial_candy - candy_taken
    result = remaining_candy
    return result

print(solution())