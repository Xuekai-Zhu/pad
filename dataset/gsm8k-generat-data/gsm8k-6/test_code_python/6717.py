def solution():
    # Find Peter's current age
    peter_mother_age = 60
    peter_age = peter_mother_age / 2

    # Find Harriet's current age
    harriet_age = (peter_age * 2) - 4  # Peter will be twice as old as Harriet in four years

    result = harriet_age
    return result

print(solution())