def solution():
    """Ricciana and Margarita joined in their school's long jump event. Ricciana ran and jumped a total of 24 feet - 20 feet for running and 4 feet for jumping. Margarita ran for 18 feet and jumped 1 foot less than twice Ricciana's jump. How much farther did Margarita run and jump than Ricciana?"""
    ricciana_run = 20
    ricciana_jump = 4
    ricciana_total = ricciana_run + ricciana_jump
    margarita_run = 18
    margarita_jump = 2 * ricciana_jump - 1
    margarita_total = margarita_run + margarita_jump
    difference = margarita_total - ricciana_total
    result = difference
    return result

print(solution())