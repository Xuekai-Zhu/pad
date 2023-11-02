def solution():
    total_questions = 20
    bill_questions = total_questions / 6  # 4 types of problems, Bill composes 1/6 of total
    ryan_questions = bill_questions * 2
    frank_questions = ryan_questions * 3

    # Calculate how many problems of each type Frank composes
    type1 = frank_questions / 4
    type2 = frank_questions / 4
    type3 = frank_questions / 4
    type4 = frank_questions / 4

    result = (type1, type2, type3, type4)
    return result

print(solution())