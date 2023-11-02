def solution():
    # Calculate the total number of stickers given to the three friends
    stickers_friends = 4 * 3  

    # Calculate the number of stickers given to Mandy and Justin
    stickers_mandy = stickers_friends + 2  
    stickers_justin = stickers_mandy - 10  

    # Calculate the total number of stickers given away
    stickers_given = stickers_friends + stickers_mandy + stickers_justin  

    # Calculate the number of stickers left with Colton
    stickers_left = 72 - stickers_given
    result = stickers_left
    return result

print(solution())