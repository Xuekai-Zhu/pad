def solution():
    """For every 5 people that attend a poetry class, the teacher gives one of the students a lollipop. If 45 people show up for class, then another 15 come in a while later, how many lollipops did the teacher give away?"""
    # Calculate the number of lollipops given away for the first 45 people
    lollipops_45 = 45 // 5

    # Calculate the number of lollipops given away for the additional 15 people
    lollipops_15 = 15 // 5

    # Calculate the total number of lollipops given away
    total_lollipops = lollipops_45 + lollipops_15

    # Display the total number of lollipops given away
    result = total_lollipops
    return result

print(solution())