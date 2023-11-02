def solution():
    num_sharks_pelican_bay = 60
    ratio_pelican_shark = 2
    moved_pelicans = 1 / 3

    # Calculate the number of Pelicans in Pelican Bay
    num_pelicans_pelican_bay = num_sharks_pelican_bay * ratio_pelican_shark

    # Calculate the number of Pelicans that have moved from Shark Bite Cove to Pelican Bay
    num_moved_pelicans = num_pelicans_pelican_bay * moved_pelicans

    # Calculate the new number of Pelicans in Shark Bite Cove
    num_pelicans_shark_bite_cove = num_pelicans_pelican_bay - num_moved_pelicans
    result = num_pelicans_shark_bite_cove
    return result

print(solution())