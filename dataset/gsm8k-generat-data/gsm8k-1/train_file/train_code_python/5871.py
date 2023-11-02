def solution():
    """If John travels 15 miles on a bike ride, and Jill travels 5 miles less, how many miles does Jim travel if he travels only 20% as far as Jill?"""
    john_miles = 15
    jill_miles = john_miles - 5
    jim_percent = 20
    jim_miles = jill_miles * (jim_percent / 100)
    result = jim_miles
    return result

print(solution())