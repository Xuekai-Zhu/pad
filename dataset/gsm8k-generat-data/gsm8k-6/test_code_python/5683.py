def solution():
    # Calculate the total distance of the three runners who are not Katarina
    total_distance = 195 - 51  # Four runners ran a combined total of 195 miles last week and Katarina ran 51 miles
    harriet_distance = total_distance / 3  # Tomas, Tyler, and Harriet all ran the same distance

    result = harriet_distance
    return result

print(solution())