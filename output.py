def write_output(name, proj_roles):
    file = open(name, "w")

    file.write(str(len(proj_roles.keys())) + "\n")
    for key, value in proj_roles.items():
        file.write(str(key) + "\n")
        roles = ""
        for person in value:
            roles += person + " "
        roles = roles.rstrip()
        file.write(roles)
        file.write("\n")

    file.close()

def write_output_maar_dan_goed(name, proj_roles):
    file = open(name, "w")

    file.write(str(len(proj_roles)) + "\n")
    for ding in proj_roles:
        file.write(str(ding[0].name) + "\n")
        roles = ""
        for person in ding[1]:
            roles += person.name + " "
        roles = roles.rstrip()
        file.write(roles)
        file.write("\n")

    file.close()