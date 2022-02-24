from hashcodeParser import parse_file
import output


if __name__ == '__main__':
    mensen,projecten=parse_file("input/a_an_example.in.txt")
    skills_to_mens=dict()
    for i in mensen:
        for j in i.skills_list:
            if j[0] not in skills_to_mens:
                skills_to_mens[j[0]]=list()
            skills_to_mens[j[0]].append(j)
    print("a")


