def solution():
    # Calculate the amount of money Steve takes home after taxes, healthcare, and union dues.
    take_home = 40000 * 0.8 * 0.9 - 800  # 20% lost to taxes, 10% lost to healthcare, and 800$ lost to union dues
    result = take_home
    return result

print(solution())