def solution():
    """Adam bought 15 apples on Monday. On Tuesday he bought 3 times that quantity. On Wednesday he bought 4 times the quantity he bought on Tuesday. What is the total quantity Adam bought on these three days?"""
    monday_apple_count = 15
    tuesday_apple_count = monday_apple_count * 3
    wednesday_apple_count = tuesday_apple_count * 4
    total_apple_count = monday_apple_count + tuesday_apple_count + wednesday_apple_count
    result = total_apple_count
    return result

print(solution())