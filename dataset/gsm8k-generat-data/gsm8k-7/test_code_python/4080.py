def solution():
    num_cookies = 50
    num_kept = 10
    num_given = 8
    num_people = 16

    # Calculate the total number of cookies Karen will have left to give to her class
    num_left = num_cookies - (num_kept + num_given)

    # Calculate the number of cookies each person in Karen's class will receive
    cookies_per_person = num_left / num_people
    result = cookies_per_person
    return result

print(solution())