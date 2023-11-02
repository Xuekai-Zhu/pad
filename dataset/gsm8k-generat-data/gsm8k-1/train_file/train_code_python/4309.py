def solution():
    """Ten percent less than twice the total number of students present in the science class yesterday have attended class today. If there were 70 students in the class yesterday and 30 students are absent today, calculate the number of students registered for the course."""
    num_present_yesterday = 70
    num_absent_today = 30
    twice_present = 2 * num_present_yesterday
    ten_percent_less = 0.1 * twice_present
    num_attending_today = twice_present - ten_percent_less - num_absent_today
    num_registered = num_present_yesterday + num_attending_today
    result = num_registered
    return result

print(solution())