def solution():
    # Calculate the amount Ofelia will save in May
    saved = 10  # amount she saved in January
    for month in range(2, 6):  # iterate through February to May
        saved *= 2  # save twice the amount from the previous month
    result = saved
    return result

print(solution())