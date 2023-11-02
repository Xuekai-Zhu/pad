def solution():
    """For many years, the number of sharks in Pelican Bay has been twice the number of Pelicans in Shark Bite Cove. But today scientists say one-third of the Pelicans in Shark Bite Cove have moved to Pelican Bay. If there are still 60 sharks in Pelican Bay, how many Pelicans remain in Shark Bite Cove?"""
    sharks_in_pelican_bay = 60
    pelicans_in_shark_bite_cove = sharks_in_pelican_bay / 2
    moved_pelicans = pelicans_in_shark_bite_cove / 3
    remaining_pelicans = pelicans_in_shark_bite_cove - moved_pelicans
    result = remaining_pelicans
    return result

print(solution())