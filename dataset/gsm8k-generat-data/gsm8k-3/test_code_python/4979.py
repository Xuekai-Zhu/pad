def solution():
    """Annie spends 2 hours a week on chess club, 8 hours a week on drama club, and 3 hours a week on glee club. If there are 12 weeks in each semester and Annie takes the first two weeks off sick, how many hours of extracurriculars does she do before midterms?"""
    # Define the number of hours Annie spends on each club per week
    chess_hours = 2
    drama_hours = 8
    glee_hours = 3

    # Define the number of weeks in each semester and the number of weeks Annie takes off sick
    num_weeks = 12
    sick_weeks = 2

    # Calculate the total number of weeks Annie participates in extracurriculars before midterms
    weeks_before_midterms = num_weeks - sick_weeks

    # Calculate the total number of hours Annie spends on extracurriculars before midterms
    total_hours = (chess_hours + drama_hours + glee_hours) * weeks_before_midterms

    # Display the total number of hours
    result = total_hours
    return result

print(solution())