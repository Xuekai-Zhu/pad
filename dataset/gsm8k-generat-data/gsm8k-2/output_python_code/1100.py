def solution():
    """Beckett is 12 and is three years younger than Olaf, while Shannen is two years younger than Olaf. If Jack is five more than twice as old as Shannen, what is the sum of the ages of all 4 people?"""
    beckett_age = 12
    olaf_age = beckett_age + 3
    shannen_age = olaf_age - 2
    jack_age = 2 * shannen_age + 5
    total_age = beckett_age + olaf_age + shannen_age + jack_age
    result = total_age
    return result

print(solution())