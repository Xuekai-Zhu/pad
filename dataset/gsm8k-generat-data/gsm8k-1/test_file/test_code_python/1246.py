def solution():
    """Samantha's last name has three fewer letters than Bobbie's last name. If Bobbie took two letters off her last name, she would have a last name twice the length of Jamie's. Jamie's full name is Jamie Grey. How many letters are in Samantha's last name?"""
    jamie_name = "Jamie Grey"
    bobbie_name = jamie_name.replace("Grey", "")
    bobbie_name = bobbie_name + "twice"
    samantha_name = bobbie_name[:-3] + "three"
    result = len(samantha_name)

    return result


def solution():
    """Mitchell is making nachos for his family. He buys two bags of chips with 55 chips each. If his family has five members, how many chips does each person get if they all get the same number?"""
    bags_of_chips = 2
    chips_per_bag = 55
    number_of_people = 5
    
    total_chips = bags_of_chips * chips_per_bag
    chips_per_person = total_chips // number_of_people
    
    result = chips_per_person
    return result

print(solution())