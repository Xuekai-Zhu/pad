def solution():
    """Peter and Kristin are to read 20 fantasy novels each in a week. Peter can read three times as fast as Kristin. If Peter reads one book in 18 hours, how long will Kristin read half of her books?"""
    peter_time_per_book = 18
    kristin_time_per_book = peter_time_per_book * 3
    kristin_half_books = 20 / 2
    kristin_total_time = kristin_half_books * kristin_time_per_book
    result = kristin_total_time
    return result

print(solution())