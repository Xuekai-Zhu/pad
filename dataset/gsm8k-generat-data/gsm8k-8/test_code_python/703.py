def solution():
    # Define the number of avocados already had and bought
    avocados_already_had = 5
    avocados_bought = 4

    # Calculate the total number of avocados
    total_avocados = avocados_already_had + avocados_bought

    # Calculate the number of servings of guacamole
    servings = total_avocados // 3

    result = servings
    return result

print(solution())