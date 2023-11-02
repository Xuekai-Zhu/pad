def solution():
    """Elois needs 4 bananas to make 1 loaf of banana bread. On Monday, she makes 3 loaves of banana bread. On Tuesday, she makes twice as many loaves of banana bread as Monday. How many bananas did she use to make all the banana bread?"""
    bananas_per_loaf = 4
    monday_loaves = 3
    tuesday_loaves = monday_loaves * 2
    total_loaves = monday_loaves + tuesday_loaves
    total_bananas = total_loaves * bananas_per_loaf
    result = total_bananas
    return result

print(solution())