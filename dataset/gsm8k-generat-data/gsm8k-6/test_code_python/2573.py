def solution():
    total_questions = 20

    # Bill composes 20/7 (rounded up) questions per type
    bill_questions_per_type = -(-total_questions // 7)

    # Ryan composes twice as many questions as Bill, so he composes 40/7 questions per type
    ryan_questions_per_type = 2 * bill_questions_per_type

    # Frank composes three times as many questions as Ryan, so he composes 120/7 questions per type
    frank_questions_per_type = 3 * ryan_questions_per_type

    result = (frank_questions_per_type, ryan_questions_per_type, bill_questions_per_type)
    return result

print(solution())