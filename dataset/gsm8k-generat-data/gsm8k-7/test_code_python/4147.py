def solution():
    initial_collection = 3000
    mike_gift = 17
    harry_gift = 2 * mike_gift + 10

    # Calculate the total number of stamps Tom receives from his friends
    total_gifts = mike_gift + harry_gift

    # Calculate the new total number of stamps in Tom's collection
    new_collection = initial_collection + total_gifts
    result = new_collection
    return result

print(solution())