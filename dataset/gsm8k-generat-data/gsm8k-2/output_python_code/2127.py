def solution():
    """A jug needs 40 cups of water to be full. A custodian at Truman Elementary School has to fill water jugs for 200 students, who drink 10 cups of water in a day. How many water jugs will the custodian fill with cups of water to provide the students with all the water they need in a day?"""
    total_cups_per_day = 200 * 10
    jugs_per_day = total_cups_per_day / 40
    result = jugs_per_day
    return result

print(solution())