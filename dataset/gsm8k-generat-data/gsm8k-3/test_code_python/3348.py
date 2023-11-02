def solution():
    """Skyler is a composer. He wrote 25 hit songs that made it on the top 10 charts; ten more songs that made it on the top 100 charts than the hit songs; 5 fewer songs than the hit songs that were never released. How many songs did Skyler write in all?"""
    # Define the number of hit songs
    hit_songs = 25
    
    # Calculate the number of songs that made it on the top 100 charts
    top_100_songs = hit_songs + 10
    
    # Calculate the number of unreleased songs
    unreleased_songs = hit_songs - 5
    
    # Calculate the total number of songs
    total_songs = hit_songs + top_100_songs + unreleased_songs
    
    # Display the total number of songs
    result = total_songs
    return result

print(solution())