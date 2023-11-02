def solution():
    """Fiona completed 36 math questions in an hour. Shirley was able to complete twice as many math questions within that same time, and Kiana completed half of the sum of Fiona and Shirley's math questions. If they each did the same number of questions the following hour, how many math questions did all three girls complete in 2 hours?"""
    # Define the initial number of math questions completed by Fiona
    fiona = 36

    # Calculate the number of math questions completed by Shirley
    shirley = fiona * 2

    # Calculate the sum of math questions completed by Fiona and Shirley
    fiona_shirley_sum = fiona + shirley

    # Calculate the number of math questions completed by Kiana
    kiana = fiona_shirley_sum / 2

    # Calculate the total number of math questions completed by all three girls in one hour
    total_questions = fiona + shirley + kiana

    # Calculate the total number of math questions completed by all three girls in two hours
    total_questions_2_hours = total_questions * 2

    result = total_questions_2_hours
    return result

print(solution())