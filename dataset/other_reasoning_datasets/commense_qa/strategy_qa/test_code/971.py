def solution():
    goblin_shark_diet = ["fish", "cephalopods", "crustaceans"]
    vegan_diet = []
    if not set(goblin_shark_diet).intersection(vegan_diet):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())