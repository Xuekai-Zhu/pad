def solution():
    """At the beginning of the day, Principal Kumar instructed Harold to raise the flag up the flagpole. The flagpole is 60 feet long, and when fully raised, the flag sits on the very top of the flagpole. Later that morning, Vice-principal Zizi instructed Harold to lower the flag to half-mast. So, Harold lowered the flag halfway down the pole. Later, Principal Kumar told Harold to raise the flag to the top of the pole once again, and Harold did just that. At the end of the day, Vice-principal Zizi instructed Harold to completely lower the flag, take it off of the pole, and put it away for the evening. Over the course of the day, how far, in feet, had the flag moved up and down the pole?"""
    flagpole_height = 60
    full_flag_height = flagpole_height
    half_flag_height = flagpole_height / 2
    total_distance = full_flag_height + half_flag_height + full_flag_height + flagpole_height
    result = total_distance
    return result

print(solution())