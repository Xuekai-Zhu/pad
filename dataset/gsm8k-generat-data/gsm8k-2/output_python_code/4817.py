def solution():
    """Peggy has 6 dolls. Her grandmother gives Peggy her own collection of 30 dolls. Over the year, Peggy receives half that amount of dolls between her birthday and Christmas. How many dolls does Peggy now have?"""
    start_dolls = 6
    grandma_dolls = 30
    additional_dolls = 0.5 * grandma_dolls
    total_dolls = start_dolls + grandma_dolls + additional_dolls
    result = total_dolls
    return result

print(solution())