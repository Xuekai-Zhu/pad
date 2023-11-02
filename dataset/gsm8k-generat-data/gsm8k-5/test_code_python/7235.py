def solution():
    # Let's assume Charlie's current age is x. 
    # Then Jenny's current age would be x+5 and Bobby's current age would be x-3.
    # We want to find out how old Charlie will be when Jenny becomes twice as old as Bobby.

    # Let's say after y years, Jenny becomes twice as old as Bobby. 
    # Then we can set up the equation (x+5+y) = 2*(x-3+y)
    # Solving for y, we get y = 8
    # This means, in 8 years, Jenny will be twice as old as Bobby.

    # Now, let's find out how old Charlie will be in 8 years.
    # Charlie's current age is x, so in 8 years, he will be x+8 years old.
    result = x+8
    return result

print(solution())