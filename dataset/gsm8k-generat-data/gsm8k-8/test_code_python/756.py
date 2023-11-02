def solution():
    # Anna's current collection
    anna_collection = 37

    # Alison gives half her collection to Anna
    alison_collection = 28
    anna_collection += alison_collection / 2

    # Jeff trades 2 bluebird stamps for 1 mountain stamp
    jeff_collection = 31
    anna_collection += 2
    jeff_collection -= 2
    anna_collection -= 1
    jeff_collection += 1

    result = anna_collection
    return result

print(solution())