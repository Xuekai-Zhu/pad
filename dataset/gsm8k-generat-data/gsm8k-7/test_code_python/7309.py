def solution():
    aaron_scarves = 10
    aaron_sweaters = 5
    enid_sweaters = 8

    scarves_wool = 3
    sweater_wool = 4

    # Calculate the total number of wool balls used by Aaron
    aaron_wool = (aaron_scarves * scarves_wool) + (aaron_sweaters * sweater_wool)

    # Calculate the total number of wool balls used by Enid
    enid_wool = enid_sweaters * sweater_wool

    # Calculate the total number of wool balls used by both Aaron and Enid
    total_wool = aaron_wool + enid_wool
    result = total_wool
    return result

print(solution())