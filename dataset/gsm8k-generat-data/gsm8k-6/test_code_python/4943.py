def solution():
    # Calculate the total number of half-gallons of milk Juan needs
    milk_per_cookie = 10/40  # Juan needs 10 half-gallons of milk for 40 cookies
    milk_per_dozen = milk_per_cookie * 12
    milk_for_200_dozen = milk_per_dozen * 200
    result = milk_for_200_dozen
    return result

print(solution())