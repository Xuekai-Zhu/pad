def solution():
    # Define the location of The Hague and the body of water it borders
    the_hague_location = "Western Netherlands"
    bordering_body_of_water = "North Sea"
    
    # Check if The Hague borders multiple bodies of water
    if bordering_body_of_water in the_hague_location:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())