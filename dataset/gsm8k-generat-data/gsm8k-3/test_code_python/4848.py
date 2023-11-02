def solution():
    """At Sarah's job 60% of the employees are women and the rest are men. Of the men, 75% have a college degree and 8 do not. How many women work at Sarah's company?"""
    # Define the percentage of women at the company
    WOMEN_PERCENTAGE = 0.6

    # Calculate the percentage of men at the company
    MEN_PERCENTAGE = 1 - WOMEN_PERCENTAGE

    # Calculate the percentage of men with a college degree
    MEN_WITH_COLLEGE_PERCENTAGE = 0.75

    # Calculate the percentage of men without a college degree
    MEN_WITHOUT_COLLEGE_PERCENTAGE = 1 - MEN_WITH_COLLEGE_PERCENTAGE

    # Calculate the total number of men at the company
    total_men = 8 / MEN_WITHOUT_COLLEGE_PERCENTAGE

    # Calculate the total number of employees at the company
    total_employees = total_men / MEN_PERCENTAGE

    # Calculate the total number of women at the company
    total_women = total_employees * WOMEN_PERCENTAGE

    # Display the total number of women
    result = total_women
    return result

print(solution())