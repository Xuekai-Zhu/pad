def solution():
    
    sharks_in_pelican_bay = 60
    pelicans_in_shark_bite_cove = sharks_in_pelican_bay / 2
    pelicans_moved_to_pelican_bay = pelicans_in_shark_bite_cove / 3
    pelicans_in_shark_bite_cove_remaining = pelicans_in_shark_bite_cove - pelicans_moved_to_pelican_bay
    result = pelicans_in_shark_bite_cove_remaining
    return result

print(solution())