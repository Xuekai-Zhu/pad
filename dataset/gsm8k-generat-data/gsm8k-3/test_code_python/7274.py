def solution():
    """20% of the job candidates at a temp agency have experience with Excel. 70% of the candidates are only willing to work day shifts. If a manager picks a candidate at random, what are the odds they know Excel and are willing to work nights?"""
    # Define the probability of a candidate having Excel experience and being willing to work nights
    excel_and_nights = 0.1

    # Define the probability of a candidate having Excel experience
    excel = 0.2

    # Define the probability of a candidate being willing to work nights given they don't have Excel experience
    nights_given_no_excel = 0.3

    # Define the probability of a candidate not having Excel experience
    no_excel = 0.8

    # Define the probability of a candidate being willing to work only day shifts
    day_shifts = 0.7

    # Calculate the probability of a candidate being willing to work nights given they have Excel experience
    nights_given_excel = (excel_and_nights / excel)

    # Calculate the probability of a candidate having Excel experience and being willing to work either night or day shifts
    excel_and_shifts = (excel * (1 - day_shifts)) + (excel * nights_given_excel)

    # Calculate the probability of a candidate being picked at random and having Excel experience and being willing to work nights
    result = excel_and_nights / excel_and_shifts
    return result

print(solution())