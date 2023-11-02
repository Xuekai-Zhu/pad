def solution():
    """Eve had 20 pieces of pomelos. After giving her friend some pomelos, Eve is left with 1/4 of the pomelos she originally had. How many pomelos did Eve give away?"""
    original_pomelos = 20
    remaining_pomelos = original_pomelos / 4
    given_pomelos = original_pomelos - remaining_pomelos
    result = given_pomelos
    return result

print(solution())