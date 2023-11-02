def solution():
    """Ricciana and Margarita joined in their school's long jump event. Ricciana ran and jumped a total of 24 feet - 20 feet for running and 4 feet for jumping. Margarita ran for 18 feet and jumped 1 foot less than twice Ricciana's jump. How much farther did Margarita run and jump than Ricciana?"""
    # Calculate Ricciana's total jump distance
    ricciana_jump = 4

    # Calculate Ricciana's total run distance
    ricciana_run = 20

    # Calculate Margarita's jump distance
    margarita_jump = 2 * ricciana_jump - 1

    # Calculate Margarita's total jump and run distance
    margarita_total = margarita_run + margarita_jump

    # Calculate the difference between Margarita and Ricciana's total distance
    difference = margarita_total - (ricciana_run + ricciana_jump)

    # return the result
    result = difference
    return result

print(solution())