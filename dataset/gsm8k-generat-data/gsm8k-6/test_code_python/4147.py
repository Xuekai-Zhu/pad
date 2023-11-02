def solution():
    # Calculate the number of stamps in Tom's collection after receiving gifts from Mike and Harry
    harry_gift = 10 + 2*17  # Harry's gift is 10 more stamps than twice Mike's gift
    total_gift = harry_gift + 17  # add Mike's gift to Harry's gift
    new_total = 3000 + total_gift  # add the total gift to the original number of stamps in Tom's collection
    result = new_total
    return result

print(solution())