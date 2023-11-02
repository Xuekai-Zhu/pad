def solution():
    """Ten percent less than twice the total number of students present in the science class yesterday have attended class today. If there were 70 students in the class yesterday and 30 students are absent today, calculate the number of students registered for the course."""
    present_yesterday = 70
    absent_today = 30
    total_today = (2*present_yesterday - (0.1*2*present_yesterday)) - absent_today
    result = total_today
    return result

print(solution())