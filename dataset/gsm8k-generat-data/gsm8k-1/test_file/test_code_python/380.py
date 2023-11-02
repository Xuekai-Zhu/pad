def solution():
    """Mr. Ruther sold 3/5 of his land and had 12.8 hectares left. How much land did he have at first?"""
    hectares_left = 12.8
    percent_remaining = 2/5
    total_hectares = hectares_left / percent_remaining
    result = total_hectares
    return result

print(solution())