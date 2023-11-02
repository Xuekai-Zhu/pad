def solution():
    boys = 50
    girls = boys + (2/5 * boys)  # 2/5 times more girls than boys
    total_students = boys + girls
    driver = 1
    assistant = 1
    total_people = total_students + driver + assistant
    result = total_people
    return result

print(solution())