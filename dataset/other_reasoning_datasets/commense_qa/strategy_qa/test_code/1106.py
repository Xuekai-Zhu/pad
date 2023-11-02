def solution():
    deadly_sins = ["Pride", "Envy", "Wrath", "Sloth", "Greed", "Gluttony", "Lust"]
    catholicism_adherents = True
    if "Pride" in deadly_sins and catholicism_adherents:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())