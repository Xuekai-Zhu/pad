def solution():
    initial_oranges = 10  # Sofia and her mother buy 10kgs of oranges
    additional_oranges = 5  # They add 5 more kgs for their neighbor

    total_oranges = initial_oranges + additional_oranges  # Total oranges for the first week
    total_oranges *= 2  # Double the weekly supply for the next two weeks

    # Total quantity of oranges bought in three weeks
    total_quantity = total_oranges * 3

    result = total_quantity
    return result

print(solution())