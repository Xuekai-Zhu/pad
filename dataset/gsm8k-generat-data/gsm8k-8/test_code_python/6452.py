def solution():
    # Start with 10 water bottles
    num_bottles = 10

    # Lose 2 at school
    num_bottles -= 2

    # Someone steals 1 at dance practice
    num_bottles -= 1

    # Put 3 stickers on each remaining bottle
    num_stickers = 3 * num_bottles

    result = num_stickers
    return result

print(solution())