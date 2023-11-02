def solution():
    initial_volume = 40  # Mary starts with 40 ounces of raw spinach
    final_volume = initial_volume * 0.2  # Mary cooks the spinach until it's 20% of its initial volume
    total_volume = final_volume + 6 + 4  # Mary mixes the spinach with 6 ounces of cream cheese and 4 ounces of eggs

    result = total_volume
    return result

print(solution())