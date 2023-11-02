def solution():
    """Four classmates were comparing their ages based on their birth month. They found out that Jolyn is 2 months older than Therese while Therese is 5 months older than Aivo. Then, Leon is 2 months older than Aivo. How much older in months is Jolyn than Leon?"""
    therese_age = 0
    aivo_age = therese_age - 5
    jolyn_age = therese_age + 2
    leon_age = aivo_age + 2
    jolyn_older_than_leon = jolyn_age - leon_age
    result = jolyn_older_than_leon
    return result

print(solution())