def solution():
    total_dolls = 60

    # Calculate Ivy's number of dolls
    ivy_dolls = total_dolls / 3

    # Calculate the number of collectors edition dolls Ivy has
    collectors_dolls = (2/3) * ivy_dolls

    result = collectors_dolls
    return result

print(solution())