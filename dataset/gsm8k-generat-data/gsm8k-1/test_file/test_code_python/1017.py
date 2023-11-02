Unfortunately, we cannot provide a solution for the Samantha's last name question as there is not enough information to determine the length of Bobbie's last name or Jamie's last name.

Here is the solution for the quiz question:

def solution():
    """In a 60-item quiz, 40% of the questions are easy, and the rest are equally divided as average and difficult questions. If Aries is sure to get 75% of the easy questions, and half of the average and difficult questions correctly, how many points is she sure to get?"""
    total_questions = 60
    easy_questions = int(total_questions * 0.4)
    avg_diff_questions = total_questions - easy_questions
    easy_score = int(easy_questions * 0.75)
    avg_diff_score = int(avg_diff_questions * 0.5)
    total_score = easy_score + avg_diff_score
    result = total_score
    return result

print(solution())