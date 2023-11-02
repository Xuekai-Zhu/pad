def solution():
    # Define the current number of sharks in Pelican Bay
    sharks_in_pelican_bay = 60

    # Calculate the previous number of pelicans in Shark Bite Cove
    previous_pelicans_in_shark_bite_cove = sharks_in_pelican_bay * 0.5

    # Calculate the number of pelicans that moved to Pelican Bay
    moved_pelicans = previous_pelicans_in_shark_bite_cove * (1/3)

    # Calculate the current number of pelicans in Shark Bite Cove
    current_pelicans_in_shark_bite_cove = previous_pelicans_in_shark_bite_cove - moved_pelicans

    result = current_pelicans_in_shark_bite_cove
    return result

print(solution())