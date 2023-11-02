def solution():
    # Calculate the total number of string cheeses needed for 4 weeks
    total_cheeses = (2 + 1) * 5 * 4  # two for oldest, one for youngest, 5 days a week, 4 weeks
    # Calculate the number of packages needed
    packages_needed = (total_cheeses // 30) + 1  # each package has 30, round up to the nearest package
    result = packages_needed
    return result

print(solution())