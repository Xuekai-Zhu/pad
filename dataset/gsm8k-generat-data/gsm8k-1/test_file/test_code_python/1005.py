def solution():
    """Brook Hills High School currently enrolls 3000 students. Half of these students are over 16 years old, and one-fourth of the students over 16 years old are male. The remaining half of the students are under 16 years old, and one-half of the students under 16 are male. In total, how many female students are enrolled at this school?"""
    total_students = 3000
    over_16 = total_students / 2
    over_16_male = over_16 / 4
    over_16_female = over_16 - over_16_male
    under_16 = total_students / 2
    under_16_male = under_16 / 2
    under_16_female = under_16 - under_16_male
    total_female = over_16_female + under_16_female
    result = total_female
    
    return result

Question: Samantha's last name has three fewer letters than Bobbie's last name. If Bobbie took two letters off her last name, she would have a last name twice the length of Jamie's. Jamie's full name is Jamie Grey. How many letters are in Samantha's last name?
Solution: 
def solution():
    """Samantha's last name has three fewer letters than Bobbie's last name. If Bobbie took two letters off her last name, she would have a last name twice the length of Jamie's. Jamie's full name is Jamie Grey. How many letters are in Samantha's last name?"""
    jamie_last_name_len = len("Grey")
    bobbie_last_name_len = jamie_last_name_len * 2 + 2
    samantha_last_name_len = bobbie_last_name_len - 3
    result = samantha_last_name_len
    
    return result

print(solution())