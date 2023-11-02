def solution():
    """In Professor Plum's biology class there are 40 students. Of those students, 80 percent have puppies. Of those who have puppies, 25% also have parrots. How many students have both puppies and parrots?"""
    total_students = 40
    puppy_percent = 0.8
    parrot_percent = 0.25
    puppy_owners = total_students * puppy_percent
    puppy_and_parrot_owners = puppy_owners * parrot_percent
    result = puppy_and_parrot_owners
    return result

print(solution())