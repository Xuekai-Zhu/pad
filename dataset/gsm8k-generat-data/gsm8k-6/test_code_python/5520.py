def solution():
    base_price = 1500
    peripherals_price = base_price * (1/5)
    upgraded_video_card_price = 300 * 2
    total_price = base_price + peripherals_price + upgraded_video_card_price
    result = total_price
    return result

print(solution())