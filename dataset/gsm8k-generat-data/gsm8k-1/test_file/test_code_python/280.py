def solution():
    """Alani's family decided that the children should write stories of any kind. They were then required to read all of the stories they'd written to the family at the end of the weekend. Alani wrote 20 stories in the first week, her brother Braylen wrote 40 stories, and her sister Margot wrote 60 stories. If they each doubled the number of stories they'd written in the first week in the second week, calculate the total number of stories they wrote altogether."""
    alani_stories = 20
    braylen_stories = 40
    margot_stories = 60
    doubled_alani_stories = alani_stories * 2
    doubled_braylen_stories = braylen_stories * 2
    doubled_margot_stories = margot_stories * 2
    total_stories = (alani_stories + doubled_alani_stories) + (braylen_stories + doubled_braylen_stories) + (margot_stories + doubled_margot_stories)
    result = total_stories
    return result

print(solution())