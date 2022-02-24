def calc_order(mensen, projecten):

    succesvolle_projecten = list()
    for project in projecten:
        if (projec)
        people = list()
        possible = True
        ordered_roles = []
        size = len(project.roles)
        while len(ordered_roles) < size:
            max_skill = 0
            nec_role = None
            for role in project.roles:
                if role[1] > max_skill:
                    max_skill = role[1]
                    nec_role = role
            ordered_roles.append(nec_role)
            project.roles.remove(nec_role)

        available_mensen = set(mensen)
        for role in ordered_roles:
            assigned = False
            for mens in mensen:
                if mens in available_mensen:
                    for skill in mens.skills_list:
                        if mens.name == "FionaN":
                            print(role[0], skill[0])
                            print(role[1], skill[1])
                        if skill[0] == role[0] and role[1] <= skill[1]:
                            people.append(mens)
                            available_mensen.remove(mens)
                            assigned = True
                            break
                if assigned:
                    break
            if not assigned:
                possible = False
                break
        if possible:
            succesvolle_projecten.append((project, people))

    print(succesvolle_projecten[0])
    return succesvolle_projecten