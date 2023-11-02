def solution():
    """Anderson makes mud masks for spa treatments. In every batch of mud that he mixes, he adds three sprigs of mint, and he adds two green tea leaves for every sprig of mint. He had to switch to a different kind of mud, which makes the other ingredients he adds half as effective. How many green tea leaves should Anderson add to a new batch of mud to get the same efficacy as before?"""
    mint_sprigs = 3
    green_tea_per_mint = 2
    old_efficiency = mint_sprigs * (green_tea_per_mint * mint_sprigs)
    new_efficiency = old_efficiency / 2
    new_green_tea_per_mint = new_efficiency / mint_sprigs
    result = new_green_tea_per_mint
    return result

print(solution())