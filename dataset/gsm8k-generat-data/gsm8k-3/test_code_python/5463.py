def solution():
    """The fifth grade class at Rosa Parks Elementary School is holding a food drive. Half the students in Ms. Perez's class collected 12 cans each, two students didn't collect any, and the remaining 13 students students each collected 4 cans. If Ms. Perez's class has 30 students, how many cans did they collect total?"""
    # Calculate the number of students who collected 12 cans each
    num_12_can_collectors = 0.5 * 30

    # Calculate the total number of cans collected by those students
    total_cans_12_can_collectors = num_12_can_collectors * 12

    # Calculate the total number of cans collected by the two students who didn't collect any cans
    total_cans_no_collectors = 2 * 0

    # Calculate the total number of cans collected by the remaining 13 students who collected 4 cans each
    total_cans_4_can_collectors = 13 * 4

    # Calculate the total number of cans collected by the entire class
    total_cans = total_cans_12_can_collectors + total_cans_no_collectors + total_cans_4_can_collectors

    # Display the total number of cans collected
    result = total_cans
    return result

print(solution())