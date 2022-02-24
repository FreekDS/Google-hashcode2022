from hashcodeParser import *
from output import write_output


"""
Output = {project : [mensen]}
"""


def get_mens_met_score(skill, score, mensen):
    mens: human
    for mens in mensen:
        skills = [tup[0] for tup in mens.skills_list]
        scores = [tup[1] for tup in mens.skills_list]
        if skill not in skills:
            continue
        for i, skill in enumerate(mens.skills_list):
            if scores[i] >= score:
                return mens, i
    return (None, None)


files = [
    'input/a_an_example.in.txt',
    'input/b_better_start_small.in.txt'
]

mensen, projecten = parse_file('input/a_an_example.in.txt')
print(mensen)

projecten.sort(key=lambda project: project.score, reverse=True)

results = {

}

for project in projecten:

    project_mensen = []

    for required_skill in project.roles:
        mens, index = get_mens_met_score(required_skill[0], required_skill[1], mensen)
        if mens:
            print("jep")
            project_mensen.append(mens.name)
            mensen.remove(mens)
    if project_mensen:
        if len(project_mensen) >= len(project.roles):
            results[project.name] = project_mensen



write_output("output1.txt", results)
