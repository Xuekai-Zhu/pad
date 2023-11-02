def solution():
    """Peter plans to go to the movies this week. He always gets a ticket for $7 and popcorn for $7. If he has 42 dollars for the week, how many times can he go to the movies?"""
    ticket_price = 7
    popcorn_price = 7
    total_price = ticket_price + popcorn_price
    budget = 42
    max_visits = budget // total_price
    result = max_visits
    return result


def solution():
    """Samantha's last name has three fewer letters than Bobbie's last name. If Bobbie took two letters off her last name, she would have a last name twice the length of Jamie's. Jamie's full name is Jamie Grey. How many letters are in Samantha's last name?"""
    jamies_last_name = 'Grey'
    bobbies_last_name = jamies_last_name * 2
    bobbies_last_name = bobbies_last_name[:-2]
    samanthas_last_name = bobbies_last_name[:-3]
    result = len(samanthas_last_name)
    return result

print(solution())