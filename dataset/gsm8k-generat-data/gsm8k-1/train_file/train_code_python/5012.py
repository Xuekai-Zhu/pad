def solution():
    """There are 50 staplers in the stapler. Stacie staples 3 dozen reports on her desk. How many staplers are left in the stapler?"""
    staplers_start = 50
    reports_stapled = 3 * 12  # 3 dozen reports
    staplers_left = staplers_start - reports_stapled
    result = staplers_left
    return result

print(solution())