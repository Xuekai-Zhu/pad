def solution():
    nathan_speed = 25/1  # Nathan can write 25 letters in 1 hour
    jacob_speed = nathan_speed * 2  # Jacob can write twice as fast as Nathan

    # Calculate the total number of letters written by Nathan in 10 hours
    total_letters_nathan = nathan_speed * 10

    # Calculate the total number of letters written by Jacob in 10 hours
    total_letters_jacob = jacob_speed * 10

    # Calculate the total number of letters the two can write together in 10 hours
    total_letters_together = total_letters_nathan + total_letters_jacob
    result = total_letters_together
    return result

print(solution())