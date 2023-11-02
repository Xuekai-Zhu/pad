def solution():
    avocados_needed = 3  # Georgie needs 3 avocados for one serving of guacamole
    avocados_owned = 5  # Georgie already has 5 avocados
    avocados_bought = 4  # Georgie's sister buys 4 more avocados

    # Calculate the total number of avocados Georgie has now
    total_avocados = avocados_owned + avocados_bought

    # Calculate the total number of servings of guacamole Georgie can make
    total_servings = total_avocados // avocados_needed
    result = total_servings
    return result

print(solution())