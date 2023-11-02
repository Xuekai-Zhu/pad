def solution():
    # Define the total length of the fence and the amount whitewashed by Ben
    initial_length = 100
    ben_length = 10

    # Calculate the length remaining after Ben whitewashes his section
    remaining_length = initial_length - ben_length

    # Calculate the length whitewashed by Billy
    billy_length = remaining_length * (1/5)

    # Calculate the length remaining after Billy whitewashes his section
    remaining_length = remaining_length - billy_length

    # Calculate the length whitewashed by Johnny
    johnny_length = remaining_length * (1/3)

    # Calculate the total length still needing to be whitewashed
    remaining_length = remaining_length - johnny_length
    result = remaining_length
    return result

print(solution())