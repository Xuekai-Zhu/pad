def solution():
    """Ruiz can make 120 pounds of chocolates in two hours. Marissa makes 3/4 times as many pounds of chocolates in an hour as Ruiz makes in the two hours. If they worked for 12 hours in a day, calculate the total amount of chocolate pounds they made together."""
    ruiz_pounds_per_hour = 120 / 2
    marissa_pounds_per_hour = 3/4 * ruiz_pounds_per_hour
    
    total_pounds = 0
    for i in range(12):
        total_pounds += ruiz_pounds_per_hour + marissa_pounds_per_hour
    
    result = total_pounds
    return result

def solution():
    """Samantha's last name has three fewer letters than Bobbie's last name. If Bobbie took two letters off her last name, she would have a last name twice the length of Jamie's. Jamie's full name is Jamie Grey. How many letters are in Samantha's last name?"""
    jamie_name_length = len("Grey")
    bobbie_name_length = 2 * jamie_name_length + 2
    samantha_name_length = bobbie_name_length - 3
    result = samantha_name_length
    return result

print(solution())