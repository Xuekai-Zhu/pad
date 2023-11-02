def solution():
    """A jar of jellybeans has 14 blue jellybeans, 26 purple jellybeans and 40 orange jellybeans. If there are 200 jellybeans in the jar, how many are there of the red color?"""
    total_jellybeans = 200
    blue_jellybeans = 14
    purple_jellybeans = 26
    orange_jellybeans = 40
    red_jellybeans = total_jellybeans - blue_jellybeans - purple_jellybeans - orange_jellybeans
    result = red_jellybeans
    return result

print(solution())