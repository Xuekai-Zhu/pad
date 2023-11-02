def solution():
    initial_cow_count = 200
    increase_percentage = 0.5

    # Calculate the number of cows born in the first year
    first_year_increase = initial_cow_count * increase_percentage

    # Add the number of new cows to the initial count to get the new total
    new_total_cow_count = initial_cow_count + first_year_increase

    # Calculate the number of cows born in the second year
    second_year_increase = new_total_cow_count * increase_percentage

    # Add the number of new cows to the updated count to get the final total
    final_total_cow_count = new_total_cow_count + second_year_increase
    result = final_total_cow_count
    return result

print(solution())