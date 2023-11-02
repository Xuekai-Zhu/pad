def solution():
    """Fiona completed 36 math questions in an hour. Shirley was able to complete twice as many math questions within that same time, and Kiana completed half of the sum of Fiona and Shirley's math questions. If they each did the same number of questions the following hour, how many math questions did all three girls complete in 2 hours?"""
    # Define the number of math questions Fiona completed in one hour
    fiona_questions = 36

    # Calculate the number of math questions Shirley completed in one hour
    shirley_questions = fiona_questions * 2

    # Calculate the total number of math questions Fiona and Shirley completed in one hour
    total_questions = fiona_questions + shirley_questions

    # Calculate the number of math questions Kiana completed in one hour
    kiana_questions = total_questions / 2

    # Calculate the total number of math questions all three girls completed in one hour
    total_questions = fiona_questions + shirley_questions + kiana_questions

    # Calculate the total number of math questions all three girls completed in two hours
    total_questions *= 2

    # Display the total number of math questions all three girls completed in two hours
    result = total_questions
    return result

print(solution())