def solution():
    """Will buys 15 oranges. When he gets home, he asks his 2 sons to wash as many oranges as they are years old. The oldest son is 8 years old, the youngest is half as old as the oldest. How many oranges are left unwashed?"""
    total_oranges = 15
    oldest_son_age = 8
    youngest_son_age = oldest_son_age / 2
    oranges_washed = oldest_son_age + youngest_son_age
    oranges_left = total_oranges - oranges_washed
    result = oranges_left
    return result

print(solution())