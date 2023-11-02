def solution():
    # Calculate the total number of songs released in 3 years
    total_songs = 3 * 12 * 3  # 3 songs per month, for 12 months per year, for 3 years

    # Calculate the total amount of money Seal gets for all the songs
    total_money = total_songs * 2000  # $2000 per song

    result = total_money
    return result

print(solution())