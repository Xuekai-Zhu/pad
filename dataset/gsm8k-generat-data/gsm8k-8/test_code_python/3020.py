def solution():
    # Calculate the amount of fish caught today
    today_fish = 2 * 80

    # Calculate the total amount of fish caught in the past four months including today
    total_fish = today_fish + 80

    # Calculate the total earnings from selling fish in the past four months including today
    earnings = total_fish * 20

    result = earnings
    return result

print(solution())