def solution():
    
    sharks_in_pelican_bay = 60
    pelicans_in_shark_bite_cove = sharks_in_pelican_bay / 2
    moved_pelicans = pelicans_in_shark_bite_cove / 3
    remaining_pelicans = pelicans_in_shark_bite_cove - moved_pelicans
    result = remaining_pelicans
    return result

print(solution())