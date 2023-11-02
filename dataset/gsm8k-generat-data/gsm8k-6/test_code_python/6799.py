def solution():
    # Calculate the number of Samsung and iPhone cell phones sold
    samsung_sold = 14 - 10 + 2  # 2 Samsung cell phones were damaged and thrown out
    iphone_sold = 8 - 5 + 1  # 1 iPhone had a manufacturing defect and was thrown out
    total_sold = samsung_sold + iphone_sold

    result = total_sold
    return result

print(solution())