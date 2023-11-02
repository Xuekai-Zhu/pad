def solution():
    """Fern is checking IDs to get into an R-rated movie. She denied 20% of the 120 kids from Riverside High, 70% of the 90 kids from West Side High, and half the 50 kids from Mountaintop High. How many kids got into the movie?"""
    kids_ Riverside = 120
    percent_denied_Riverside = 20
    kids_denied_Riverside = kids_Riverside * (percent_denied_Riverside / 100)
    kids_allowed_Riverside = kids_Riverside - kids_denied_Riverside
    
    kids_West_Side = 90
    percent_denied_West_Side = 70
    kids_denied_West_Side = kids_West_Side * (percent_denied_West_Side / 100)
    kids_allowed_West_Side = kids_West_Side - kids_denied_West_Side
    
    kids_Mountaintop = 50
    percent_denied_Mountaintop = 50
    kids_denied_Mountaintop = kids_Mountaintop * (percent_

print(solution())