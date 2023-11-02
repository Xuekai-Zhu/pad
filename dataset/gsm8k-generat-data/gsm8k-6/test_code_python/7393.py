def solution():
    # Calculate the number of cookies Paul took out each day
    cookies_per_day = (70 - 28) / 7  # Paul took out the same amount each day for a week
    cookies_in_four_days = cookies_per_day * 4  # Calculate the number of cookies Paul took out in four days

    result = cookies_in_four_days
    return result

print(solution())