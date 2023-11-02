def solution():
    hours_per_week = 30  # The artist spends 30 hours every week painting
    hours_per_painting = 3  # It takes the artist 3 hours to complete a painting
    weeks = 4  # The artist wants to know how many paintings she can make in 4 weeks

    # Calculate the total number of paintings the artist can make in 4 weeks
    total_paintings = (hours_per_week * weeks) / hours_per_painting
    result = total_paintings
    return result

print(solution())