def solution():
    # Calculate the number of pistachios with shells and opened shells
    shells_pistachios = 0.95 * 80  # 95% of pistachios have shells
    opened_pistachios = 0.75 * shells_pistachios  # 75% of those with shells have opened shells
    result = opened_pistachios
    return result

print(solution())