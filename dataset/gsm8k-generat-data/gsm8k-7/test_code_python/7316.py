def solution():
    num_jars = 4
    jar_capacity = 12
    num_cucumbers = 10
    cucumbers_to_pickles = 6
    vinegar_per_jar = 10
    total_vinegar = 100

    # Calculate the total number of pickles that can be made with the available cucumbers
    total_pickles = num_cucumbers * cucumbers_to_pickles

    # Calculate the total number of jars needed to store all pickles
    total_jars = int(total_pickles / jar_capacity) + (1 if total_pickles % jar_capacity > 0 else 0)

    # Calculate the total amount of vinegar needed
    total_vinegar_needed = total_jars * vinegar_per_jar

    # Calculate the number of ounces of vinegar left
    vinegar_left = total_vinegar - total_vinegar_needed
    result = vinegar_left
    return result

print(solution())