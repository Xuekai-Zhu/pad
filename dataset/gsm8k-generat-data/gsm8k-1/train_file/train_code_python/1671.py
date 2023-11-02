def solution():
    """In two years, Ophelia will be four times as old as Lennon. If Lennon is currently eight years old, how old is Ophelia?"""
    lennon_age = 8
    ophelia_multiplier = 4
    ophelia_age_in_two_years = lennon_age * ophelia_multiplier
    ophelia_age = ophelia_age_in_two_years - 2 * 2 # subtracting 2 years twice to get current age
    result = ophelia_age
    
    return result

print(solution())