def solution():
    num_strawberries_per_pie = 3

    # Calculate the total number of pounds of strawberries they picked
    christine_picked = 10
    rachel_picked = christine_picked * 2
    total_picked = christine_picked + rachel_picked

    # Calculate the total number of pies they can make
    total_pies = total_picked // num_strawberries_per_pie

    result = total_pies
    return result

print(solution())