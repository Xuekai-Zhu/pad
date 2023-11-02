def solution():
    """Jim reads at a rate of 40 pages an hour. He reads a total of 600 pages per week. He increases his reading speed to 150% of its former speed but reads 4 hours less per week. How many pages does he read a week now?"""
    original_speed = 40
    original_hours = 600 / original_speed
    new_speed = original_speed * 1.5
    new_hours = original_hours - 4
    new_pages = new_speed * new_hours
    result = new_pages
    return result

print(solution())