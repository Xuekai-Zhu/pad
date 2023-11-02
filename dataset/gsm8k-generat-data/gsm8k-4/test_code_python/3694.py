def solution():
    """For many years, the number of sharks in Pelican Bay has been twice the number of Pelicans in Shark Bite Cove. But today scientists say one-third of the Pelicans in Shark Bite Cove have moved to Pelican Bay. If there are still 60 sharks in Pelican Bay, how many Pelicans remain in Shark Bite Cove?"""
    # Define the initial number of sharks in Pelican Bay
    sharks_pelican_bay = 60

    # Define the initial ratio of sharks to pelicans
    ratio = 2

    # Calculate the initial number of pelicans in Shark Bite Cove
    pelicans_shark_bite_cove = sharks_pelican_bay / ratio

    # Calculate the number of pelicans that moved to Pelican Bay
    pelicans_moved = pelicans_shark_bite_cove / 3

    # Calculate the remaining number of pelicans in Shark Bite Cove
    pelicans_shark_bite_cove_remaining = pelicans_shark_bite_cove - pelicans_moved

    result = pelicans_shark_bite_cove_remaining
    return result

print(solution())