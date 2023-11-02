def solution():
    """Cameron guides tour groups in a museum. He usually answers two questions per tourist. Today, he did four tours. The early morning first group was only 6 people. The following group was a busy group of 11. The third group had 8 people, but one was inquisitive and asked three times as many questions as usual. The last group of the day was a late group of 7. How many questions did Cameron answer?"""
    tours = 4
    people_tour_one = 6
    people_tour_two = 11
    people_tour_three = 8
    inquisitive_person = 1
    multiplier = 3
    people_tour_four = 7
    questions_per_person = 2

    total_questions = (people_tour_one + people_tour_two + ((people_tour_three - inquisitive_person) * questions_per_person)
                       + (inquisitive_person * questions_per_person * multiplier) + (people_tour_four * questions_per_person))
    result = total_questions

    return result

print(solution())