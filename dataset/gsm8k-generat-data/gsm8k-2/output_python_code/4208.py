def solution():
    """Valerie’s cookie recipe makes 16 dozen cookies and calls for 4 pounds of butter. She only wants to make 4 dozen cookies for the weekend. How many pounds of butter will she need?"""
    original_recipe = 16 * 4  # 64 dozen cookies
    butter_per_dozen = 4 / 16  # 0.25 pounds of butter per dozen
    weekend_recipe = 4 * butter_per_dozen  # 1 pound of butter for 4 dozen cookies
    result = weekend_recipe
    return result

print(solution())