def solution():
    # Calculate the number of nice people in the crowd
    nice_Barry = 24  # all people named Barry are nice
    nice_Kevin = 0.5 * 20  # only half of people named Kevin are nice
    nice_Julie = 0.75 * 80  # three-fourths of people named Julie are nice
    nice_Joe = 0.1 * 50  # 10% of people named Joe are nice
    total_nice_people = nice_Barry + nice_Kevin + nice_Julie + nice_Joe
    result = total_nice_people
    return result

print(solution())