def solution():
    initial_volume = 220
    leak_percent = 0.1  # 10% leak
    remaining_percent = 1 - leak_percent

    # Calculate the remaining volume after the leak
    remaining_volume = initial_volume * remaining_percent
    result = remaining_volume
    return result

print(solution())