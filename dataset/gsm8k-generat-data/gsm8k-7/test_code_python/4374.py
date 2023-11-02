def solution():
    servings_per_jar = 15
    num_people = 2  # Phoebe and her dog
    servings_per_day = num_people

    num_days = 30

    # Calculate the total number of servings needed for 30 days
    total_servings = num_days * servings_per_day

    # Calculate the total number of jars needed
    num_jars = total_servings / servings_per_jar
    result = num_jars
    return result

print(solution())