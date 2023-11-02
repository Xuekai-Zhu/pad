def solution():
    walk_time = 1  # Each walk takes 1 hour
    walk_distance = 4  # Each walk covers 4 miles
    days_in_March = 31  # There are 31 days in March

    # Calculate the total number of walks in March
    total_walks = days_in_March - 4  # Emberly didn't walk for 4 days in March

    # Calculate the total distance Emberly walked in March
    total_distance = total_walks * walk_distance
    result = total_distance
    return result

print(solution())