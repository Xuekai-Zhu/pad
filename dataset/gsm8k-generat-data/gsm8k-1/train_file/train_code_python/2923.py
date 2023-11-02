def solution():
    """Madeline has 10 flowers. If 4 flowers are red, 2 flowers are white, and the rest are blue, what percentage of flowers are blue?"""
    total_flowers = 10
    red_flowers = 4
    white_flowers = 2
    blue_flowers = total_flowers - red_flowers - white_flowers
    percentage_blue = (blue_flowers / total_flowers) * 100
    result = percentage_blue
    return result

print(solution())