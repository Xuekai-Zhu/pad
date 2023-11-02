def solution():
    """Noel bakes 4 dozen donuts for his class. There are 30 students in class, but only 80% like donuts. How many donuts does each student who likes donuts get to eat?"""
    donuts_per_dozen = 12
    total_donuts = 4 * donuts_per_dozen
    num_donut_likes = int(30 * 0.8)
    donuts_per_student = total_donuts // num_donut_likes
    result = donuts_per_student
    return result

print(solution())