def solution():
    # Calculate the total number of corn stalks
    total_stalks = 5 * 80  # 5 rows of corn, each row has 80 corn stalks.

    # Calculate the total number of bushels of corn
    total_bushels = total_stalks // 8  # About every 8 corn stalks will produce a bushel of corn.

    result = total_bushels
    return result

print(solution())