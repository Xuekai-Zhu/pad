def solution():
    """Elvis is releasing a new album with 10 songs, but he doesn't want to waste too much time on writing. He spends 5 hours in the studio, where he writes, records, and edits his songs. Each song takes 12 minutes to record, then it takes 30 minutes to edit all of his songs. How many minutes did it take Elvis to write each song, if each song took the same amount of time to write?"""
    # Define the total time Elvis spends in the studio in minutes
    studio_time = 5 * 60

    # Define the time it takes to record one song
    record_time = 12

    # Define the time it takes to edit all songs
    edit_time = 30

    # Calculate the total time Elvis spends recording
    total_record_time = record_time * 10

    # Calculate the total time Elvis spends editing
    total_edit_time = edit_time

    # Calculate the remaining time for writing
    remaining_time = studio_time - total_record_time - total_edit_time

    # Calculate the time for writing one song
    write_time = remaining_time / 10

    # return the result
    result = write_time
    return result

print(solution())