def solution():
    """Four classmates were comparing their ages based on their birth month. They found out that Jolyn is 2 months older than Therese while Therese is 5 months older than Aivo. Then, Leon is 2 months older than Aivo. How much older in months is Jolyn than Leon?"""
    jolyn_to_therese = 2
    therese_to_aivo = 5
    aivo_to_leon = 2
    jolyn_to_leon = jolyn_to_therese + therese_to_aivo + aivo_to_leon
    result = jolyn_to_leon
    return result

print(solution())