import copy

def calc_order(mensen, projecten):

    succesvolle_projecten = list()
    for project in projecten:
        if (project.name == "ShoppingProv8"):
            print(project.roles)
        assignments = list()
        possible = True
        ordered_roles = []
        copy_roles = copy.deepcopy(project.roles)
        size = len(project.roles)
        while len(ordered_roles) < size:
            max_skill = 0
            nec_role = None
            for role in copy_roles:
                if role[1] > max_skill:
                    max_skill = role[1]
                    nec_role = role
            ordered_roles.append(nec_role)
            copy_roles.remove(nec_role)

        available_mensen = set(mensen)
        for role in ordered_roles:
            assigned = False
            for mens in mensen:
                if mens in available_mensen:
                    for skill in mens.skills_list:
                        if skill[0] == role[0] and role[1] <= skill[1]:
                            assignments.append((role[0], mens))
                            available_mensen.remove(mens)
                            assigned = True
                            break
                if assigned:
                    break
            if not assigned:
                possible = False
                break
        if possible:
            people = list()
            for role in project.roles:
                for assignment in assignments:
                    if assignment[0] == role[0]:
                        people.append(assignment[1])
            succesvolle_projecten.append((project, people))

    return succesvolle_projecten