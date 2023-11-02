def solution():
    """A class of 30 high school students is preparing for a field trip. If each student contributes $2 every Friday for their trip, how many dollars will they have in 2 months?"""
    students = 30
    contribution_per_student = 2
    weeks_in_two_months = 8
    total_contributions = students * contribution_per_student * weeks_in_two_months
    result = total_contributions
    return result

print(solution())