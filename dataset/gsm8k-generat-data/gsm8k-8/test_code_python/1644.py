def solution():
    # Calculate the total number of pictures taken
    total_pictures = 10*365*3

    # Calculate the number of memory cards needed
    num_cards = total_pictures // 50
    if total_pictures % 50 != 0:
        num_cards += 1

    # Calculate the total cost of the memory cards
    cost = num_cards * 60
    result = cost
    return result

print(solution())