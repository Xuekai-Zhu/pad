def solution():
    
    total_employees = 100
    drive_to_work = int(total_employees * 0.6)
    dont_drive = total_employees - drive_to_work
    public_transportation = dont_drive // 2
    result = public_transportation
    return result

print(solution())