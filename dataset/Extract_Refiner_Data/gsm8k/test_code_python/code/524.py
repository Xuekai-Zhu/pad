def solution():
    
    # Define the number of sofas Ophelia has
    ophelia_sofas = 20

    # Calculate the number of chairs they have
    chairs = ophelia_sofas / 2

    # Calculate the number of chairs Jenna has
    jenna_chairs = 3 * ophelia_chairs

    # Calculate the total number of sofas and chairs
    total_sofas = ophelia_sofas + chairs

    # Display the total number of sofas and chairs
    result = total_sofas + jenna_chairs
    return result

print(solution())