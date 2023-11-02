def solution():
    """Peggy has 6 dolls. Her grandmother gives Peggy her own collection of 30 dolls. Over the year, Peggy receives half that amount of dolls between her birthday and Christmas. How many dolls does Peggy now have?"""
    initial_dolls = 6
    grandmother_dolls = 30
    additional_dolls = grandmother_dolls / 2
    total_dolls = initial_dolls + grandmother_dolls + additional_dolls
    result = total_dolls
    return result

print(solution())