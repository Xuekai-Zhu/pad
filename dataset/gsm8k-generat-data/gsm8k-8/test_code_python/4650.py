def solution():
    sandwiches_eaten_on_saturday = 2
    sandwiches_eaten_on_sunday = 1

    # Calculate the total number of sandwiches eaten
    total_sandwiches = sandwiches_eaten_on_saturday + sandwiches_eaten_on_sunday

    # Calculate the total number of bread pieces consumed
    bread_pieces_consumed = total_sandwiches * 2

    result = bread_pieces_consumed
    return result

print(solution())