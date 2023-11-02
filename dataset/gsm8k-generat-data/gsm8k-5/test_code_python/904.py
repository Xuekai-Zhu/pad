def solution():
    juice_per_lime = 1/16  # 1 lime yields 1/16 cup of juice, which equals 1 tablespoon
    juice_per_pie = 1/4 * 2  # Audrey wants to double the amount of key lime juice

    # Calculate the number of limes Audrey needs for one pie
    limes_per_pie = juice_per_pie / juice_per_lime

    result = limes_per_pie
    return result

print(solution())