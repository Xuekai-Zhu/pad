def solution():
    original_price = 1200
    old_card_price = 300
    new_card_price = 500

    # Calculate the total cost of the new video card
    total_card_cost = new_card_price - old_card_price

    # Calculate the final cost of the computer after replacing the video card
    final_price = original_price + total_card_cost
    result = final_price
    return result

print(solution())