def solution():
    # Define the number of fires each firefighter has put out
    doug_fires = 20
    kai_fires = 3 * doug_fires
    eli_fires = 0.5 * kai_fires

    # Calculate the total number of fires put out
    total_fires = doug_fires + kai_fires + eli_fires
    result = total_fires
    return result

print(solution())