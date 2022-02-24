import output
from hashcodeParser import parse_file


def checkviable(project, skills_to_mens):
    humans_used = list()
    for i in project.roles:
        found = False
        for mens in skills_to_mens[i[0]]:
            if (found): break
            for sk in mens.skills_list:
                if (sk[0] == i[0] and sk[1] >= i[1]):
                    if (mens not in humans_used):
                        found = True
                        humans_used.append(mens)
                        break
        if (not found):
            for check in project.roles:
                if found:
                    break
                if (check[0] == i[0] and check[1] > i[1]):
                    if (i[0] == 1):
                        for key in skills_to_mens.keys():
                            if found:
                                break
                            for mens in skills_to_mens[key]:
                                if mens not in humans_used:
                                    humans_used.append(mens)
                                    found = True
                                    break
                    else:
                        for mens in skills_to_mens[i[0]]:
                            if (found): break
                            for sk in mens.skills_list:
                                if (sk[0] == i[0] and sk[1] - 1 >= i[1]):
                                    if (mens not in humans_used):
                                        found = True
                                        humans_used.append(mens)
                                        break
            if (not found):
                return False
    return True


def getMensen(project, skills_to_mens):
    toreturn = list()
    humans_used = list()
    for i in project.roles:
        found = False
        mens_found = None
        for mens in skills_to_mens[i[0]]:
            if (mens in humans_used):
                continue
            for sk in mens.skills_list:
                if (sk[0] == i[0] and sk[1] >= i[1]):
                    found = True
                    if (mens_found == None):
                        mens_found = mens
                    else:
                        if (mens_found.get_skill(i[0])[1] > sk[1]):
                            mens_found = mens
                    break
        if (found):
            humans_used.append(mens_found)
            toreturn.append((mens_found, i))
        else:
            # print("what the frick, der is hier ne mens dat niet gevonden wordt")
            training = False
            for check in project.roles:
                if (check[0] == i[0] and check[1] > i[1]):
                    training = True
            if training:
                if (i[0] == 1):
                    for key in skills_to_mens.keys():
                        if found:
                            break
                        for mens in skills_to_mens[key]:
                            if found:
                                break
                            if mens not in humans_used:
                                mens_found = mens
                                found = True
                else:
                    for mens in skills_to_mens[i[0]]:
                        if (mens in humans_used):
                            continue
                        for sk in mens.skills_list:
                            if (sk[0] == i[0] and sk[1] >= i[1] - 1):
                                found = True
                                if (mens_found == None):
                                    mens_found = mens
                                else:
                                    if (mens_found.get_skill(i[0])[1] > sk[1]):
                                        mens_found = mens
                                break
            else:
                return False
    return toreturn


def den_heuristic(project, den_dag: int):
    score = project.score
    if (den_dag + project.time > project.best_before):
        score -= (project.time) - (den_dag + project.best_before) ** 0.2
    return score


def solve(file: str):
    projects_with_assignment = list()
    mensen, projecten = parse_file(file)
    projecten.sort(key=lambda project: den_heuristic(project, 0), reverse=True)
    skills_to_mens = rekenen(mensen)
    print("a")
    current = 0
    den_dag = 0
    while (True):
        if (current > len(projecten) - 1):
            break
        eens_zien = projecten[current]
        if (checkviable(eens_zien, skills_to_mens)):
            mensen = getMensen(eens_zien, skills_to_mens)
            if (isinstance(mensen, bool)):
                current += 1
                continue
            projects_with_assignment.append((eens_zien, mensen))
            del projecten[current]
            for i in mensen:
                i[0].increment_skill(i[1][0], i[1][1])
            current = 0
            den_dag += eens_zien.time
            projecten.sort(key=lambda project: den_heuristic(project, den_dag), reverse=True)
        current += 1
    print("a")
    den_output = list()
    for i in projects_with_assignment:
        new_list = list()
        for j in i[1]:
            new_list.append(j[0])
        den_output.append((i[0], new_list))
    return den_output


def rekenen(mensen):
    skills_to_mens = dict()
    for i in mensen:
        for j in i.skills_list:
            if j[0] not in skills_to_mens:
                skills_to_mens[j[0]] = list()
            skills_to_mens[j[0]].append(i)
    return skills_to_mens


if __name__ == '__main__':
    files = [
        # 'input/a_an_example.in.txt',
        # 'input/b_better_start_small.in.txt',
        # 'input/c_collaboration.in.txt',
        # 'input/d_dense_schedule.in.txt',
        # 'input/e_exceptional_skills.in.txt',
        'input/f_find_great_mentors.in.txt',
    ]
    for file in files:
        den_output = solve(file)
        output.write_output_maar_dan_goed(file[6:] + ".out", den_output)
