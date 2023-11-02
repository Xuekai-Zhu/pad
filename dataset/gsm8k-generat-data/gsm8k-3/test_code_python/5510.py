def solution():
    """Karl, Ryan, and Ben are fond of collecting stickers. Karl has 25 stickers. Ryan has 20 more stickers than Karl. Ben has 10 fewer stickers than Ryan. They placed all their stickers in one sticker book. How many stickers did they place altogether?"""
    
    # Define the number of stickers each person has
    karl_stickers = 25
    ryan_stickers = karl_stickers + 20
    ben_stickers = ryan_stickers - 10
    
    # Calculate the total number of stickers
    total_stickers = karl_stickers + ryan_stickers + ben_stickers
    
    # Display the total number of stickers
    result = total_stickers
    return result

print(solution())