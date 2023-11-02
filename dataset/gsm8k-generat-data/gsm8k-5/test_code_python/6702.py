def solution():
    total_attendees = 100  # 100 people attended the dance
    faculty_staff = round(total_attendees * 0.1)  # 10% of attendees were faculty/staff
    remaining_attendees = total_attendees - faculty_staff  # Remaining attendees after subtracting faculty/staff
    girls = round(remaining_attendees * (2/3))  # 2/3 of remaining attendees were girls
    boys = remaining_attendees - girls  # Remaining attendees after subtracting girls

    result = boys
    return result

print(solution())