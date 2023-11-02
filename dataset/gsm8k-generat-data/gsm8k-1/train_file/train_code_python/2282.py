def solution():
    """Sebastian plays drums for percussion in an orchestra. He sits next to the brass section where four people play trombone, two play trumpet, and one plays a French horn. In front of them are the strings section with three violinists, a cellist, and a contrabassist. Next to the strings are a trio of clarinets and a quartet of flute players in the woodwinds section. The maestro conducts them all. How many people are in the orchestra?"""
    brass_section = 7
    strings_section = 5
    woodwinds_section = 7
    maestro = 1
    total_members = brass_section + strings_section + woodwinds_section + maestro
    result = total_members
    return result

print(solution())