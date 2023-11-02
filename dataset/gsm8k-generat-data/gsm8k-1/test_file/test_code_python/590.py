def solution():
    """A cup of mushrooms weighs 100 grams and has 3 grams of protein. If John eats 200 grams of mushrooms every day how many grams of protein does he get per week?"""
    weight_per_cup = 100
    protein_per_cup = 3
    grams_per_day = 200
    cups_per_day = grams_per_day / weight_per_cup
    protein_per_day = protein_per_cup * cups_per_day
    protein_per_week = protein_per_day * 7
    result = protein_per_week
    return result

print(solution())