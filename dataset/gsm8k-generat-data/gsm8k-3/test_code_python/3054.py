def solution():
    """John has 10 members of his family on his father's side.  His mother's side is 30% larger.  How many people are there in total?"""
    # Define the number of people on John's father's side
    father_side = 10

    # Calculate the number of people on John's mother's side
    mother_side = int(father_side * 1.3)

    # Calculate the total number of people
    total_people = father_side + mother_side

    # Display the total number of people
    result = total_people
    return result

print(solution())