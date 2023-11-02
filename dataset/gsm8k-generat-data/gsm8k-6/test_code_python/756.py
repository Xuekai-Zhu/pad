def solution():
    # Find how many stamps Alison gives to Anna
    alison_to_anna = 28 / 2

    # Update Anna's collection
    anna_collection = 37 + alison_to_anna

    # Subtract 2 bluebird stamps from Anna's collection and add 1 mountain stamp
    anna_collection = anna_collection - 2 + 1

    result = anna_collection
    return result

print(solution())