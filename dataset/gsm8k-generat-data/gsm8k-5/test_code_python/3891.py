def solution():
    total_jellybeans = 200
    blue_jellybeans = 14
    purple_jellybeans = 26
    orange_jellybeans = 40

    # Calculate the number of red jellybeans
    red_jellybeans = total_jellybeans - blue_jellybeans - purple_jellybeans - orange_jellybeans
    result = red_jellybeans
    return result

print(solution())