def solution():
    """Sebastian plays drums for percussion in an orchestra. He sits next to the brass section where four people play trombone, 
    two play trumpet, and one plays a French horn. In front of them are the strings section with three violinists, a cellist, 
    and a contrabassist. Next to the strings are a trio of clarinets and a quartet of flute players in the woodwinds section. 
    The maestro conducts them all. How many people are in the orchestra?"""
    brass_section = 4 + 2 + 1
    strings_section = 3 + 1 + 1
    woodwinds_section = 3 + 4
    percussion_section = 1
    maestro = 1
    total_members = brass_section + strings_section + woodwinds_section + percussion_section + maestro
    result = total_members
    return result

print(solution())