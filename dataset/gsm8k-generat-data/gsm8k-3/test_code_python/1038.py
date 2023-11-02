def solution():
    """Marge planted 23 seeds in her garden. Five of the seeds never grew into plants. A third of the remaining seeds grew, but the plants were eaten by squirrels and rabbits. A third of the number of uneaten plants were strangled by weeds. Marge pulled two weeds, but liked the flowers on one weed and let the plant grow as part of her garden. How many plants did Marge end up with?"""
    # Calculate the number of plants that did not grow
    no_growth = 5

    # Calculate the number of seeds that grew
    grew = (23 - no_growth) * (2/3)

    # Calculate the number of plants that were eaten
    eaten = grew * (1/3)

    # Calculate the number of uneaten plants
    uneaten = grew - eaten

    # Calculate the number of uneaten plants strangled by weeds
    strangled = uneaten * (1/3)

    # Calculate the final number of plants
    final_plants = uneaten - strangled + 1

    # Display the final number of plants
    result = final_plants
    return result

print(solution())