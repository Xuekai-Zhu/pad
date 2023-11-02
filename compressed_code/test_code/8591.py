def solution():
    
    total_employees = 100
    drive_to_work = total_employees * 0.6
    donot_drive_to_work = total_employees - drive_to_work
    public_transportation = donot_drive_to_work * 0.5
    
    result = public_transportation
    return result

print(solution())