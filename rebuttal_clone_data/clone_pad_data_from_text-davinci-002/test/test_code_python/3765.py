def solution():
    initial_collection = 10
    sold_collection = 6
    desired_collection = 4
    brother_collection = 2 * initial_collection
    total_collection = initial_collection - sold_collection + brother_collection 
    result = total_collection
    return result

print(solution())