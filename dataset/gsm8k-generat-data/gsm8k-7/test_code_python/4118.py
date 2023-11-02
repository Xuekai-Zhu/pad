def solution():
    num_guests = 12
    servings_per_pie = 8
    num_pies = 3
    apples_per_serving = 1.5

    # Calculate the total number of servings of apple pie
    total_servings = servings_per_pie * num_pies

    # Calculate the total number of apples used in the apple pies
    total_apples = total_servings * apples_per_serving

    # Calculate the average number of apples each guest ate
    avg_apples_per_guest = total_apples / num_guests
    result = avg_apples_per_guest
    return result

print(solution())