def solution():
    """Marge planted 23 seeds in her garden. Five of the seeds never grew into plants. A third of the remaining seeds grew, but the plants were eaten by squirrels and rabbits. A third of the number of uneaten plants were strangled by weeds. Marge pulled two weeds, but liked the flowers on one weed and let the plant grow as part of her garden. How many plants did Marge end up with?"""
    total_seeds = 23
    ungerminated_seeds = 5
    remaining_seeds = total_seeds - ungerminated_seeds
    eaten_plants = remaining_seeds / 3
    remaining_plants = remaining_seeds - eaten_plants
    strangled_plants = remaining_plants / 3
    uneaten_plants = remaining_plants - strangled_plants
    pulled_weeds = 2
    final_plants = uneaten_plants - pulled_weeds + 1
    result = final_plants
    return result

print(solution())