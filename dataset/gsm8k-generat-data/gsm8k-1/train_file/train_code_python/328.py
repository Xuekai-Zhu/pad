def solution():
    """Samuel bought 2 dozen doughnuts and Cathy bought 3 dozen doughnuts. They planned to share the doughnuts evenly with their 8 other friends. How many doughnuts will each of them receive?"""
    samuel_doughnuts = 2 * 12
    cathy_doughnuts = 3 * 12
    total_doughnuts = samuel_doughnuts + cathy_doughnuts
    num_people = 8 + 2 # Samuel and Cathy
    doughnuts_per_person = total_doughnuts / num_people
    result = doughnuts_per_person
    return result

print(solution())