def solution():
    aaron_scarves = 10
    aaron_sweaters = 5
    enid_sweaters = 8
    balls_per_scarf = 3
    balls_per_sweater = 4

    # Calculate total balls of wool used by Aaron
    aaron_wool = (aaron_scarves * balls_per_scarf) + (aaron_sweaters * balls_per_sweater)

    # Calculate total balls of wool used by Enid
    enid_wool = enid_sweaters * balls_per_sweater

    # Calculate total balls of wool used by both Enid and Aaron
    total_wool = aaron_wool + enid_wool
    result = total_wool
    return result

print(solution())