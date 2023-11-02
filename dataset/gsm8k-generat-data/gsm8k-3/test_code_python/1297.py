def solution():
    """In Professor Plum's biology class there are 40 students. Of those students, 80 percent have puppies. Of those who have puppies, 25% also have parrots. How many students have both puppies and parrots?"""
    # Define the number of students and the percentages
    num_students = 40
    puppy_percent = 0.8
    parrot_given_puppy_percent = 0.25

    # Calculate the number of students who have puppies
    num_puppy_owners = num_students * puppy_percent

    # Calculate the number of puppy owners who also have parrots
    num_both = num_puppy_owners * parrot_given_puppy_percent

    # Round the result to the nearest integer
    result = round(num_both)

    return result

print(solution())