def solution():
    # Calculate the number of hours Ben will work in 10 days
    total_hours_worked = 8 * 10

    # Calculate the number of chairs Ben can build in 10 days
    chairs_built = total_hours_worked // 5  # it takes him 5 hours to build 1 rocking chair
    result = chairs_built
    return result

print(solution())