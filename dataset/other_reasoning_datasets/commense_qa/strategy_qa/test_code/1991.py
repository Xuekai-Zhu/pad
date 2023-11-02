def solution():
    # Define the facts
    persians_have_multiple_desserts = True
    saffron_is_used_in_persian_desserts = True
    saffron_is_made_from_crocus_threads = True
    # Check if an ancient visitor to Persia would consume crocus threads
    if persians_have_multiple_desserts and saffron_is_used_in_persian_desserts and saffron_is_made_from_crocus_threads:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())