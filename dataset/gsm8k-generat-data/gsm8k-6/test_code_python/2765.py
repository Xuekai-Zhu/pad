def solution():
    # Calculate the total number of people who ordered vanilla ice cream
    vanilla_count = int(0.2 * 220)  # 20% of 220 people ordered vanilla ice cream
    # Calculate the number of people who ordered chocolate ice cream
    chocolate_count = (220 - vanilla_count) / 3
    result = chocolate_count
    return result

print(solution())