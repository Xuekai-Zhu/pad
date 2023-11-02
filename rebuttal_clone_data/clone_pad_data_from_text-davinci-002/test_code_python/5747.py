def solution():
    black_jellybeans = 8
    green_jellybeans = 2 + black_jellybeans
    orange_jellybeans = green_jellybeans - 1
    jellybean_count = black_jellybeans + green_jellybeans + orange_jellybeans
    result = jellybean_count
    return result

print(solution())