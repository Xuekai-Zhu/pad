def solution():
    """In Professor Plum's biology class there are 40 students. Of those students, 80 percent have puppies. Of those who have puppies, 25% also have parrots. How many students have both puppies and parrots?"""
    # Define the total number of students and the percentage of students who have puppies
    total_students = 40
    puppies_percentage = 0.8

    # Calculate the number of students who have puppies
    puppies_students = total_students * puppies_percentage

    # Calculate the number of students who have both puppies and parrots
    pp_students = puppies_students * 0.25

    # Round the result to the nearest integer
    result = round(pp_students)
    return result

print(solution())