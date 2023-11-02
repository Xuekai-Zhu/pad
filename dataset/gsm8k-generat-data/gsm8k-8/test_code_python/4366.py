def solution():
    # Define variables for the number of songs and amount of money per song
    songs_per_month = 3
    money_per_song = 2000
    
    # Calculate the total number of songs released in 3 years
    total_songs = songs_per_month * 12 * 3
    
    # Calculate the total amount of money earned in 3 years
    total_money = total_songs * money_per_song
    
    result = total_money
    return result

print(solution())