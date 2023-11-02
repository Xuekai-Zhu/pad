def solution():
    """Forest and his friends have prepared a birthday cake for their friend Juelz having 240 cake pieces.
    After singing the birthday song, they ate 60% of the cake's pieces,
    and later, Juelz divided the remaining pieces among his three sisters.
    What is the number of pieces of cake each sister received?"""
    
    #Total number of cake pieces
    total_pieces=240
    
    #Calculate the number of pieces left after 60% are eaten
    remaining_pieces=total_pieces*(1-0.6)
    
    #Divide the remaining pieces among Juelz's three sisters
    pieces_per_sister=remaining_pieces/3
    
    #Display the number of pieces each sister received
    result=pieces_per_sister
    return result

print(solution())