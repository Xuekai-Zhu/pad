def solution():
    original_posters = 14  # Two years ago, Cassidy had 14 posters
    additional_posters = 6  # After this summer, Cassidy will have 6 more posters
    doubled_size = original_posters * 2  # The current size of Cassidy's collection is double what it was two years ago
    current_posters = doubled_size - additional_posters  # Subtract the additional posters to get the current total

    result = current_posters
    return result

print(solution())