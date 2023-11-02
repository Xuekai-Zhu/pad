def solution():
    """As firefighters, Doug, Kai, and Eli have been putting out a lot of fires over the week. Doug has put out 20 fires for the week and Kai has put out 3 times more than Doug. Meanwhile, Eli has put out half the number of fires Kai was able to. How many fires have they put out for the entire week?"""
    # Define the number of fires Doug has put out
    doug_fires = 20

    # Define the number of fires Kai has put out (three times more than Doug)
    kai_fires = doug_fires * 3

    # Define the number of fires Eli has put out (half the number of fires Kai was able to)
    eli_fires = kai_fires / 2

    # Calculate the total number of fires put out by all three firefighters
    total_fires = doug_fires + kai_fires + eli_fires

    # Return the result
    result = total_fires
    return result

print(solution())