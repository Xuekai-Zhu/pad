def solution():
    """If one person can paint half a house in 5 days, how many hours would it take for 5 people to paint a whole house?"""
    days_per_half_house = 5
    people = 5
    half_house = 0.5
    whole_house = 2 * half_house
    days_per_whole_house = days_per_half_house * 2
    hours_per_whole_house = days_per_whole_house * 24
    hours_per_person = hours_per_whole_house / people
    result = hours_per_person
    return result

print(solution())