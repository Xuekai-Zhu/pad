def solution():
    """Jim reads at a rate of 40 pages an hour. He reads a total of 600 pages per week. He increases his reading speed to 150% of its former speed but reads 4 hours less per week. How many pages does he read a week now?"""
    former_speed = 40
    former_hours = 600 / former_speed
    new_speed = former_speed * 1.5
    new_hours = former_hours - 4
    new_pages = new_speed * new_hours
    result = new_pages
    return result

print(solution())