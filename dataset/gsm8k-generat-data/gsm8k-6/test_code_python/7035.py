def solution():
    # Calculate the total possible points before the final assignment
    total_possible_points = 9 * 100  # assuming each assignment was worth 100 points

    # Calculate the total points Ahmed has before the final assignment
    ahmed_points = 91 * 9  # Ahmed has 91% in the class before the final assignment

    # Calculate the total points Emily has before the final assignment
    emily_points = 92 * 9  # Emily has 92% in the class before the final assignment

    # Calculate the minimum grade Ahmed needs on the final assignment to beat Emily
    required_points = emily_points + 90 - ahmed_points  # add Emily's 90 on the final assignment and subtract Ahmed's points so far
    required_grade = (required_points / 100) + 1  # divide required points by total possible points and add 1 to get the minimum grade required
    result = int(required_grade)
    return result

print(solution())