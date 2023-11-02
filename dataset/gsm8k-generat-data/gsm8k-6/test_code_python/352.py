def solution():
    # Calculate the total number of cards and the total number of pages needed
    total_cards = 60 * 7  # 60 packs with 7 cards each
    total_pages = (total_cards + 9) // 10  # round up to the nearest whole number

    result = total_pages
    return result

print(solution())