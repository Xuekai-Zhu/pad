def solution():
    """Mr. Manuel is a campsite manager who's been tasked with checking the number of tents set up in the recreation area. On a particular day, he counted 100 tents in the northernmost part of the campsite and twice that number on the east side of the grounds. The number of tents at the center of the camp was four times the number of tents in the northernmost part of the campsite. If he also counted 200 tents in the southern part of the campsite, what is the total number of tents in the recreation area?"""
    north_tents = 100
    east_tents = 2 * north_tents
    center_tents = 4 * north_tents
    south_tents = 200
    total_tents = north_tents + east_tents + center_tents + south_tents
    result = total_tents
    return result

print(solution())