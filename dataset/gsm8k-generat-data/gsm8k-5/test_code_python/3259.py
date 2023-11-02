def solution():
    michael_money = 42  # Michael starts with $42
    brother_money = michael_money / 2  # Michael gives away half the money to his brother
    brother_money -= 3  # His brother spends $3 on candy and has $35 left

    # Calculate how much money his brother had at first
    original_brother_money = (brother_money + 3) * 2
    result = original_brother_money
    return result

print(solution())