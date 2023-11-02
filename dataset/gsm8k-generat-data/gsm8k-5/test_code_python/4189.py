def solution():
    luke_age = 20  # Luke is currently 20 years old
    mr_bernard_age = 3 * (luke_age + 8)  # In 8 years, Mr. Bernard will be 3 times as old as Luke is now
    total_age = luke_age + mr_bernard_age  # Calculate the total age
    avg_age = total_age / 2  # Calculate the average age
    result = avg_age - 10  # Calculate 10 years less than their average age
    return result

print(solution())