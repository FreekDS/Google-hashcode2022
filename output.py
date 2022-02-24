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