def solution():
    num_tours = 4
    num_questions_per_tourist = 2

    # Calculate the total number of tourists Cameron guided
    total_tourists = 6 + 11 + 8 + 7

    # Calculate the total number of questions Cameron answered for the first 3 groups
    first_3_groups = (6 + 11 + 8) * num_questions_per_tourist

    # Calculate the number of questions Cameron answered for the inquisitive tourist
    inquisitive_questions = 3 * num_questions_per_tourist

    # Calculate the total number of questions Cameron answered for all groups
    total_questions = first_3_groups + inquisitive_questions + (7 * num_questions_per_tourist)

    result = total_questions
    return result

print(solution())