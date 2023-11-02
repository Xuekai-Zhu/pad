def solution():
    """Annie spends 2 hours a week on chess club, 8 hours a week on drama club, and 3 hours a week on glee club. If there are 12 weeks in each semester and Annie takes the first two weeks off sick, how many hours of extracurriculars does she do before midterms?"""
    chess_hours = 2
    drama_hours = 8
    glee_hours = 3
    total_hours = (chess_hours + drama_hours + glee_hours) * (12 - 2)
    result = total_hours
    return result

print(solution())