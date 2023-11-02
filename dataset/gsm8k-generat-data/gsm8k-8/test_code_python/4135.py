def solution():
    # Define the number of teeth for each person
    person1_teeth = 32
    person2_teeth = 32
    person3_teeth = 32
    person4_teeth = 32

    # Calculate the number of teeth removed for each person
    person1_removed = person1_teeth * 1/4
    person2_removed = person2_teeth * 3/8
    person3_removed = person3_teeth * 1/2
    person4_removed = 4

    # Calculate the total number of teeth removed
    total_removed = person1_removed + person2_removed + person3_removed + person4_removed
    result = total_removed
    return result

print(solution())