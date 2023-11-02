def solution():
    boxes = 3 + 5
    total_grams = boxes * 225
    parrot_grams = 100
    cockatiel_grams = 50
    weekly_grams = parrot_grams + cockatiel_grams
    weeks = total_grams / weekly_grams
    result = weeks
    return result

print(solution())