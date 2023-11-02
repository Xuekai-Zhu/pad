def solution():
    """On Mondays, Wednesdays, and Fridays, college student Kimo has three 1-hour classes each day. On Tuesdays and Thursdays, he has two 2-hour classes each day. In one semester, there are 16 weeks of school. In one semester, how many hours does Kimo spend attending classes?"""
    days_per_week = 5
    weeks_per_semester = 16
    classes_per_day_mon_wf = 3
    classes_per_day_tue_thu = 2
    hours_per_class_mon_wf = 1
    hours_per_class_tue_thu = 2
    total_hours_mon_wf = classes_per_day_mon_wf * hours_per_class_mon_wf
    total_hours_tue_thu = classes_per_day_tue_thu * hours_per_class_tue_thu
    total_hours_per_week = total_hours_mon_wf * 3 + total_hours_tue_thu * 2
    total_hours_per_semester = total_hours_per_week * weeks_per_semester
    result = total_hours_per_semester
    return result

print(solution())