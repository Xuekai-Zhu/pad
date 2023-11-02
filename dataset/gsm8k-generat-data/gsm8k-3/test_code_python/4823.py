def solution():
    """As firefighters, Doug, Kai, and Eli have been putting out a lot of fires over the week. Doug has put out 20 fires for the week and Kai has put out 3 times more than Doug. Meanwhile, Eli has put out half the number of fires Kai was able to. How many fires have they put out for the entire week?"""
    # Calculate the number of fires Kai put out
    kai_fires = 3 * 20

    # Calculate the number of fires Eli put out
    eli_fires = 0.5 * kai_fires

    # Calculate the total number of fires put out
    total_fires = 20 + kai_fires + eli_fires

    # Display the total number of fires put out
    result = total_fires
    return result

print(solution())