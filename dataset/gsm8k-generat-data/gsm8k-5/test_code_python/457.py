def solution():
    fiona_questions = 36  # Fiona completed 36 math questions in an hour
    shirley_questions = fiona_questions * 2  # Shirley completed twice as many questions as Fiona
    total_questions_first_hour = fiona_questions + shirley_questions  # Total questions completed in the first hour
    kiana_questions = (fiona_questions + shirley_questions) / 2  # Kiana completed half of Fiona and Shirley's questions
    total_questions_second_hour = (fiona_questions + shirley_questions + kiana_questions) / 3  # Each girl did the same number of questions in the second hour

    # Calculate the total number of questions completed in 2 hours
    total_questions = (total_questions_first_hour + total_questions_second_hour) * 2
    result = total_questions
    return result

print(solution())