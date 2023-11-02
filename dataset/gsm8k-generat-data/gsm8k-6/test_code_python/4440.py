def solution():
    # Calculate the total number of bananas needed to make 99 loaves
    bananas_per_batter = 1  # the recipe calls for 1 banana per batter
    batters_needed = 99 / 3  # each batter makes 3 loaves
    bananas_needed = batters_needed * bananas_per_batter
    result = bananas_needed
    return result

print(solution())