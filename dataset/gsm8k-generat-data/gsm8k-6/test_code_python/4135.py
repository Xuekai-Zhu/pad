def solution():
    # Calculate the number of teeth removed for each person
    person1_teeth_removed = (1/4) * 32
    person2_teeth_removed = (3/8) * 32
    person3_teeth_removed = (1/2) * 32
    person4_teeth_removed = 4

    # Calculate the total number of teeth removed
    total_teeth_removed = person1_teeth_removed + person2_teeth_removed + person3_teeth_removed + person4_teeth_removed
    result = total_teeth_removed
    return result

print(solution())