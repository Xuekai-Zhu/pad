def solution():
    northern_tents = 100  # Number of tents in the northern part of the campsite
    eastern_tents = 2 * northern_tents  # Number of tents on the east side of the campsite
    center_tents = 4 * northern_tents  # Number of tents in the center of the campsite
    southern_tents = 200  # Number of tents in the southern part of the campsite

    # Calculate the total number of tents in the recreation area
    total_tents = northern_tents + eastern_tents + center_tents + southern_tents
    result = total_tents
    return result

print(solution())