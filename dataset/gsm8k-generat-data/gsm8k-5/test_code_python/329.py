def solution():
    samuel_doughnuts = 2 * 12  # Samuel bought 2 dozen doughnuts
    cathy_doughnuts = 3 * 12  # Cathy bought 3 dozen doughnuts
    total_doughnuts = samuel_doughnuts + cathy_doughnuts  # Calculate the total number of doughnuts
    total_people = 8 + 2  # Samuel and Cathy plus their 8 friends
    doughnuts_per_person = total_doughnuts // total_people  # Divide the doughnuts evenly among the people
    result = doughnuts_per_person
    return result

print(solution())