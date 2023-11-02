def solution():
    # Calculate the maximum number of Oreo cheesecakes that Lionel can make
    max_cheesecakes = min(14//2, 15//3) # number of boxes of Graham crackers and packets of Oreos needed for one cheesecake
    # Calculate the number of Graham crackers left over
    graham_crackers_left = 14 - (2 * max_cheesecakes)  # each cheesecake needs 2 boxes of Graham crackers
    result = graham_crackers_left
    return result

print(solution())