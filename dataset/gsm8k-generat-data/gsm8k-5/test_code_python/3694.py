def solution():
    sharks_in_pelican_bay = 60  # There are 60 sharks in Pelican Bay
    pelicans_in_pelican_bay = sharks_in_pelican_bay * 1/2  # The number of pelicans in Pelican Bay is half the number of sharks
    pelicans_in_shark_bite_cove_initial = pelicans_in_pelican_bay * 1/3  # One-third of the pelicans in Shark Bite Cove have moved to Pelican Bay
    pelicans_in_shark_bite_cove_final = pelicans_in_shark_bite_cove_initial * 2/3  # After one-third of the pelicans move, the remaining pelicans in Shark Bite Cove become two-thirds of the initial number

    result = pelicans_in_shark_bite_cove_final
    return result

print(solution())