def solution():
    num_houses = 100
    num_sunday_extras = 30
    num_sunday_skips = 10

    # Calculate the total number of papers delivered from Monday to Saturday
    mon_to_sat_papers = num_houses * 6

    # Calculate the total number of papers delivered on Sunday
    sun_papers = (num_houses - num_sunday_skips) + num_sunday_extras

    # Calculate the total number of papers delivered in a week
    total_papers = mon_to_sat_papers + sun_papers
    result = total_papers
    return result

print(solution())