def solution():
    total_ratio = 7 + 3  # The total ratio of books to pens Arlo needs to buy is 7+3=10
    total_stationery = 400  # Arlo bought a total of 400 stationery from the store

    # Calculate the number of books Arlo needs to buy using the ratio
    books_ratio = 7 / total_ratio
    books = books_ratio * total_stationery
    result = books
    return result

print(solution())