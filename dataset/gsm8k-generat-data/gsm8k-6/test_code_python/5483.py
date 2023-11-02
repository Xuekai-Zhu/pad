def solution():
    # Calculate the total number of books
    total_books = 4 * 400

    # Calculate the distance in miles
    distance = total_books / 5280  # assuming 1 mile is 5280 feet

    # Calculate the total distance Karen covers if she bikes from her home to the library and back
    total_distance = distance * 2  # assuming Karen bikes back and forth
    result = total_distance
    return result

print(solution())