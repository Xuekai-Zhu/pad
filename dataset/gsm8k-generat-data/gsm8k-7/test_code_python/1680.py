def solution():
    total_candy = 349
    talitha_candy = 108
    solomon_candy = 153

    # Calculate the total number of candy taken
    total_taken = talitha_candy + solomon_candy

    # Calculate the number of candy remaining in the bowl
    candy_remaining = total_candy - total_taken
    result = candy_remaining
    return result

print(solution())