def solution():
    # Calculate the total number of glass bottles Kyle bought
    total_bottles = 2 + 3  # 2 bought initially + 3 more bought

    # Calculate the total number of origami stars the glass bottles can hold
    stars_per_bottle = 15
    total_stars = total_bottles * stars_per_bottle

    result = total_stars
    return result

print(solution())