def solution():
    """Thomas, Toby, and Rebecca worked a total of 157 hours in one week. Thomas worked x hours. Toby worked 10 hours less than twice what Thomas worked, and Rebecca worked 8 hours less than Toby. How many hours did Rebecca work?"""
    total_hours = 157
    thomas_hours = x
    toby_hours = 2*x - 10
    rebecca_hours = toby_hours - 8
    hours_worked = thomas_hours + toby_hours + rebecca_hours
    rebecca_hours_worked = rebecca_hours
    return rebecca_hours_worked

print(solution())