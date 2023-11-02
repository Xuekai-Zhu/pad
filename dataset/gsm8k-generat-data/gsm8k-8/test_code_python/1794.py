def solution():
    # Define the ratio of Joshua's share to Justin's share
    joshua_to_justin_ratio = 3

    # Calculate the total ratio
    total_ratio = 1 + joshua_to_justin_ratio

    # Calculate Justin's share
    justin_share = 40 / total_ratio

    # Calculate Joshua's share using the ratio
    joshua_share = justin_share * joshua_to_justin_ratio
    result = joshua_share
    return result

print(solution())