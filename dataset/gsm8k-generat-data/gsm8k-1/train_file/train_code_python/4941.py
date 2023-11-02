def solution():
    """The Lady Eagles basketball team scored a total of 311 points in 5 games. Some players combined for 188 points. Lisa, Jessie, and Devin equally scored the rest. How many points did Jessie score?"""
    total_points = 311
    combined_points = 188
    remaining_points = total_points - combined_points
    jld_points = remaining_points / 3
    jessie_points = jld_points
    result = jessie_points
    return result

print(solution())