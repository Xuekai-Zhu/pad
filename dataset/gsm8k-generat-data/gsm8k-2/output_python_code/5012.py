def solution():
    """There are 50 staplers in the stapler. Stacie staples 3 dozen reports on her desk. How many staplers are left in the stapler?"""
    stapler_count = 50
    report_count = 3 * 12  # 3 dozen
    stapler_count -= report_count  # subtract the number of staples used
    result = stapler_count
    return result

print(solution())