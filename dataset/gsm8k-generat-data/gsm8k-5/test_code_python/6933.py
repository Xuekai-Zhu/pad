def solution():
    lasagna_minces = 100 * 2  # 100 lasagnas that use 2 pounds of ground mince each
    total_minces = 500  # The cafeteria has used a total of 500 pounds of ground mince
    cottage_minces = total_minces - lasagna_minces  # The remaining ground mince is used for cottage pies

    # Calculate the number of cottage pies made
    cottage_pies = cottage_minces / 3
    result = cottage_pies
    return result

print(solution())