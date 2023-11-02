def solution():
    """For every 5 people that attend a poetry class, the teacher gives one of the students a lollipop. If 45 people show up for class, then another 15 come in a while later, how many lollipops did the teacher give away?"""
    # Define the total number of people in the poetry class
    total_people = 45 + 15

    # Calculate the number of lollipops to give away
    lollipops = total_people // 5

    # Return the result
    result = lollipops
    return result

print(solution())