def solution():
    total_fish = 15 + (3 * 15)  # Mabel counts 15 fish on day one and three times as many on day two
    num_sharks = total_fish * 0.25  # Mabel knows that 25% of the fish she counts will be sharks
    result = num_sharks
    return result

print(solution())