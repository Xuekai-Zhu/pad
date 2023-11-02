def solution():
    # Calculate the total number of fruits the three children have
    oranges = 3
    apples = 2*oranges
    total_fruits = oranges + apples + (oranges + apples)  # Mark gets as many bananas as Mike and Matt received fruits altogether
    result = total_fruits
    return result

print(solution())