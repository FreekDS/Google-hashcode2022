def write_output(name, proj_roles):
    file = open(name, "w")

    file.write(len(proj_roles))
    for key, value in proj_roles.items():
        file.write(key, "\n")
        roles = ""
        for person in value:
            roles += person + " "
        roles = roles.rstrip()
        file.write(roles)
        file.write("\n")

    file.close()