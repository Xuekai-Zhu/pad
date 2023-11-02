def solution():
    """As firefighters, Doug, Kai, and Eli have been putting out a lot of fires over the week. Doug has put out 20 fires for the week and Kai has put out 3 times more than Doug. Meanwhile, Eli has put out half the number of fires Kai was able to. How many fires have they put out for the entire week?"""
    doug_fires = 20
    kai_fires = 3 * doug_fires
    eli_fires = 0.5 * kai_fires
    total_fires = doug_fires + kai_fires + eli_fires
    result = total_fires
    return result

print(solution())