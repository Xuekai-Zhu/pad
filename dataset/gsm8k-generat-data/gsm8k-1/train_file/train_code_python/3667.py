def solution():
    """Anderson makes mud masks for spa treatments. In every batch of mud that he mixes, he adds three sprigs of mint, and he adds two green tea leaves for every sprig of mint. He had to switch to a different kind of mud, which makes the other ingredients he adds half as effective. How many green tea leaves should Anderson add to a new batch of mud to get the same efficacy as before?"""
    sprigs_of_mint = 3
    tea_per_sprig = 2
    mud_efficiency = 1
    new_mud_efficiency = 0.5
    tea_needed = (sprigs_of_mint * tea_per_sprig * mud_efficiency) / (tea_per_sprig * sprigs_of_mint * new_mud_efficiency)
    result = tea_needed
    return result

print(solution())