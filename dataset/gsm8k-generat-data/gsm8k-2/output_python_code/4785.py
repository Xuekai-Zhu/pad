def solution():
    """A chocolate cake needs 3 eggs per cake. Cheesecake requires 8 eggs for each cheesecake. How many more eggs are needed for 9 cheesecakes than are needed for 5 chocolate cakes?"""
    eggs_for_chocolate_cake = 3 * 5
    eggs_for_cheesecake = 8 * 9
    eggs_difference = eggs_for_cheesecake - eggs_for_chocolate_cake
    result = eggs_difference
    return result

print(solution())