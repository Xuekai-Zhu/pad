def solution():
    """Marge planted 23 seeds in her garden. Five of the seeds never grew into plants. A third of the remaining seeds grew, but the plants were eaten by squirrels and rabbits. A third of the number of uneaten plants were strangled by weeds. Marge pulled two weeds but liked the flowers on one weed and let the plant grow as part of her garden. How many plants did Marge end up with?"""
    total_seeds = 23
    seeds_not_grown = 5
    grown_seeds = (total_seeds - seeds_not_grown) / 3
    eaten_plants = grown_seeds
    uneaten_plants = grown_seeds - eaten_plants
    strangled_plants = uneaten_plants / 3
    plants_pulled = 2
    plants_in_garden = uneaten_plants - strangled_plants + 1
    result = plants_in_garden
    return result

print(solution())