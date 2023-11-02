def solution():
    # Convert Pepe's height to feet
    pepe_height = 4.5 / 12

    # Calculate Frank's height
    frank_height = pepe_height - 0.5

    # Calculate Larry's height
    larry_height = frank_height - 1

    # Calculate Ben's height
    ben_height = larry_height - 1

    # Calculate Big Joe's height
    bigjoe_height = ben_height + 1

    result = bigjoe_height
    return result

print(solution())