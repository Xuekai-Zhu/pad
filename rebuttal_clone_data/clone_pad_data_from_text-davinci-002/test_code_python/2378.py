def solution():
    price_lego_blocks = 250
    price_toy_sword = 120
    price_play_dough = 35
    quantity_lego_blocks = 3
    quantity_toy_sword = 7
    quantity_play_dough = 10
    total_price = price_lego_blocks * quantity_lego_blocks + price_toy_sword * quantity_toy_sword + price_play_dough * quantity_play_dough
    result = total_price
    return result

print(solution())