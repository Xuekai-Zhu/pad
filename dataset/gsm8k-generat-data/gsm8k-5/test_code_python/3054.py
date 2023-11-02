def solution():
    father_side = 10  # John has 10 members on his father's side
    mother_side = int(father_side * 1.3)  # John's mother's side is 30% larger
    total_members = father_side + mother_side  # Calculate the total number of family members

    result = total_members
    return result

print(solution())