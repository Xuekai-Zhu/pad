def solution():
    """There were 349 pieces of candy in a bowl. Talitha took 108 pieces and Solomon took 153 pieces. How many pieces of candy remain in the bowl?"""
    starting_candy = 349
    talitha_candy = 108
    solomon_candy = 153
    remaining_candy = starting_candy - talitha_candy - solomon_candy
    result = remaining_candy
    return result

print(solution())