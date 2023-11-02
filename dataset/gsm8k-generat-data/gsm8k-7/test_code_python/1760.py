def solution():
    aleesia_pounds_per_week = 1.5
    aleesia_weeks = 10
    alexei_pounds_per_week = 2.5
    alexei_weeks = 8

    # Calculate the total pounds Aleesia lost
    aleesia_pounds_lost = aleesia_pounds_per_week * aleesia_weeks

    # Calculate the total pounds Alexei lost
    alexei_pounds_lost = alexei_pounds_per_week * alexei_weeks

    # Calculate the total pounds the friends lost together
    total_pounds_lost = aleesia_pounds_lost + alexei_pounds_lost
    result = total_pounds_lost
    return result

print(solution())