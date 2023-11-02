def solution():
    # Calculate the original number of Pelicans in Shark Bite Cove
    sharks_in_pelican_bay = 60  # given
    pelicans_in_shark_bite_cove = sharks_in_pelican_bay / 2  # the number of sharks in Pelican Bay has been twice the number of Pelicans in Shark Bite Cove

    # Calculate the number of Pelicans that have moved to Pelican Bay
    pelicans_moved = pelicans_in_shark_bite_cove / 3  # one-third of the Pelicans in Shark Bite Cove have moved to Pelican Bay

    # Calculate the remaining number of Pelicans in Shark Bite Cove
    remaining_pelicans = pelicans_in_shark_bite_cove - pelicans_moved

    result = remaining_pelicans
    return result

print(solution())