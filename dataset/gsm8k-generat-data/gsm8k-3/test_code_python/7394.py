def solution():
    """Mr. Manuel is a campsite manager who's been tasked with checking the number of tents set up in the recreation area. On a particular day, he counted 100 tents in the northernmost part of the campsite and twice that number on the east side of the grounds. The number of tents at the center of the camp was four times the number of tents in the northernmost part of the campsite. If he also counted 200 tents in the southern part of the campsite, what is the total number of tents in the recreation area?"""
    # Define the number of tents in the northernmost part of the campsite
    north_tents = 100

    # Calculate the number of tents on the east side of the grounds
    east_tents = north_tents * 2

    # Calculate the number of tents at the center of the camp
    center_tents = north_tents * 4

    # Define the number of tents in the southern part of the campsite
    south_tents = 200

    # Calculate the total number of tents in the recreation area
    total_tents = north_tents + east_tents + center_tents + south_tents

    # Display the total number of tents
    result = total_tents
    return result

print(solution())