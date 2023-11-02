def solution():
    total_fruit = 56  # There are 56 pieces of fruit in the box
    oranges = total_fruit / 4  # One-fourth of the box contains oranges
    peaches = oranges / 2  # There are half as many peaches as oranges
    apples = peaches * 5  # There are five times as many apples as peaches
    result = apples
    return result

print(solution())