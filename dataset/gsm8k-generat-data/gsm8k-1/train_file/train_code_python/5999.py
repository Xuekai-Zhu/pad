def solution():
    """If it takes 8 days for 3 builders to build a cottage. How long will it take 6 builders to build the same size cottage working at the same rate?"""
    days = 8
    builders = 3
    new_builders = 6
    time_taken = days * builders / new_builders
    result = time_taken
    return result

print(solution())