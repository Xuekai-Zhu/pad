def solution():
    jujutsu = "form of unarmed combat"
    janissaries = "elite infantry of the Ottoman Empire"
    janissary_gear = "chain mail and armor, sharp swords"
    if jujutsu and not janissaries:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())