def solution():
    """Andy is mixing blue, green and white paint in a 1 : 2 : 5 ratio. If he uses 6 gallons of green paint, how many gallons of paint does he use total?"""
    green_ratio = 2
    total_ratio = 1 + 2 + 5
    total_paint = (6 * total_ratio) / green_ratio
    result = total_paint
    return result

print(solution())