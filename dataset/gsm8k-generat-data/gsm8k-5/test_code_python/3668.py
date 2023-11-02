def solution():
    mint_per_batch = 3  # Anderson adds 3 sprigs of mint per batch
    tea_per_mint = 2  # Anderson adds 2 green tea leaves per sprig of mint
    old_mud_effectiveness = 1  # The old mud's effectiveness is 100%
    new_mud_effectiveness = 0.5  # The new mud's effectiveness is 50%

    # Calculate the original number of tea leaves per batch
    original_tea_per_batch = mint_per_batch * tea_per_mint

    # Calculate the new number of tea leaves per batch needed to maintain the same efficacy as before
    new_tea_per_batch = original_tea_per_batch * (old_mud_effectiveness / new_mud_effectiveness)

    result = new_tea_per_batch
    return result

print(solution())