def solution():
    expected_attendance = 50 + 40  # 50 people are confirmed, and another 40 might show up
    total_gift_bags = 10 + 20 + expected_attendance  # Carl made 10 extravagant gift bags and 20 average ones, and he needs enough for everyone

    # Calculate how many more gift bags Carl needs to make
    additional_gift_bags_needed = expected_attendance - total_gift_bags
    result = additional_gift_bags_needed
    return result

print(solution())