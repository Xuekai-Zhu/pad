def solution():
    # Calculate the total number of people who ordered vanilla ice cream
    total_vanilla = 0.2 * 220

    # Calculate the ratio of vanilla orders to chocolate orders
    vanilla_to_chocolate = 2

    # Calculate the total number of people who ordered chocolate ice cream
    total_chocolate = (220 - total_vanilla) / (vanilla_to_chocolate + 1)

    result = total_chocolate
    return result

print(solution())