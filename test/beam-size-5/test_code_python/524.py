def solution():
    
    # Define the number of sofas Ophelia has
    ophelia_sofas = 20

    # Calculate the number of chairs Jenna has
    jenna_chairs = 3 * ophelia_sofas

    # Calculate the number of sofas each person has
    ophelia_sofas_per_person = ophelia_sofas / 2
    jenna_sofas_per_person = jenna_chairs / 2

    # Calculate the total number of sofas and chairs
    total_sofas = ophelia_sofas_per_person + jenna_sofas_per_person
    result = total_sofas
    return result

print(solution())