def solution():
    total_people = 40  # There are 40 people in the race
    cycling_fraction = 3/5  # 3/5 of the people are riding bicycles
    biking_people = cycling_fraction * total_people  # Number of people riding bicycles
    triking_people = total_people - biking_people  # Number of people riding tricycles

    # Total number of wheels from bicycles and tricycles combined
    total_wheels = (2 * biking_people) + (3 * triking_people)

    result = total_wheels
    return result

print(solution())