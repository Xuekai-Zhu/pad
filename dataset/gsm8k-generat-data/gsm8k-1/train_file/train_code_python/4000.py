def solution():
    """Liza reads 20 pages in an hour, and Suzie reads 15 pages in an hour. How many more pages does Liza read than Suzie in 3 hours?"""
    liza_rate = 20
    suzie_rate = 15
    time = 3
    liza_total = liza_rate * time
    suzie_total = suzie_rate * time
    difference = liza_total - suzie_total
    result = difference
    return result

print(solution())