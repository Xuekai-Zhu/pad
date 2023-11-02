def solution():
    total_employees = 100  # The company has 100 employees
    drive_to_work = 0.6 * total_employees  # 60% of the employees drive to work
    dont_drive_to_work = total_employees - drive_to_work  # The remaining employees don't drive to work
    public_transportation = 0.5 * dont_drive_to_work  # Half of the employees who don't drive take public transportation
    result = public_transportation
    return result

print(solution())