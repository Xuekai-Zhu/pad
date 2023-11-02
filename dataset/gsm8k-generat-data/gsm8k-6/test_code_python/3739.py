def solution():
    # Calculate the number of marshmallows each child can hold
    haley = 8
    michael = 3 * haley  # Michael can hold 3 times as many as Haley
    brandon = michael / 2  # Brandon can hold half as many as Michael
    
    # Calculate the total number of marshmallows held by all three kids
    total_marshmallows = haley + michael + brandon
    result = total_marshmallows
    return result

print(solution())