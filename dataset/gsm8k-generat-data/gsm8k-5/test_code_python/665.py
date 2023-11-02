def solution():
    total_apples = 50  # Bill picked 50 apples from the orchard
    apples_given_to_kids = 2 * 2 * 3  # Bill's kids gave 3 apples each to their 2 favorite teachers
    apples_used_for_pie = 2 * 10  # Jill baked 2 apple pies, using 10 apples per pie

    # Calculate the total number of apples Bill has left
    apples_left = total_apples - apples_given_to_kids - apples_used_for_pie
    result = apples_left
    return result

print(solution())