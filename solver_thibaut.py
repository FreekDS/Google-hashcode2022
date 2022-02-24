from hashcodeParser import parse_file
import output

def checkviable(project,skills_to_mens):
    for i in project.roles:
        found=False
        if(i[1]==1):
            found= True
        else:
            for mens in skills_to_mens[i[0]]:
                for sk in mens.skills_list:
                    if(sk[0]==i[0] and sk[1]>=i[1]):
                        found = True
                        break
        if(not found):
            return False
    return True

def getMensen(project,skills_to_mens):
    toreturn=list()
    for i in project.roles:
        found = False
        mens_found=None
        if (i[1] == 1):
            found = True
        else:
            for mens in skills_to_mens[i[0]]:
                for sk in mens.skills_list:
                    if (sk[0] == i[0] and sk[1] >= i[1]):
                        found = True
                        if(mens_found==None):
                            mens_found = mens
                        else:
                            if(mens_found.get_skill(i[0])[1]>sk[1]):
                                mens_found=mens
                        break
        if (found):
            toreturn.append((mens_found,i))
    return toreturn
def solve(file:str):
    projects_with_assignment=list()
    mensen,projecten=parse_file(file)
    skills_to_mens=dict()
    for i in mensen:
        for j in i.skills_list:
            if j[0] not in skills_to_mens:
                skills_to_mens[j[0]]=list()
            skills_to_mens[j[0]].append(i)
    print("a")
    current=0
    while(True):
        if(current>len(projecten)-1):
            break
        eens_zien=projecten[current]
        if(checkviable(eens_zien,skills_to_mens)):
            current=0
            mensen=getMensen(eens_zien,skills_to_mens)
            projects_with_assignment.append((eens_zien,mensen))
            del projecten[current]
            for i in mensen:
                i[0].increment_skill(i[1][0],i[1][1])

        current+=1
    print("a")
    den_output=list()
    for i in projects_with_assignment:
        new_list=list()
        for j in i[1]:
            new_list.append(j[0])
        den_output.append((i[0],new_list))
    return den_output
if __name__ == '__main__':
    files = [
        'input/a_an_example.in.txt',
        'input/b_better_start_small.in.txt',
        'input/c_collaboration.in.txt',
        'input/d_dense_schedule.in.txt',
        'input/e_exceptional_skills.in.txt',
        'input/f_find_great_mentors.in.txt',
    ]
    for file in files:
        den_output=solve(file)
        output.write_output_maar_dan_goed(file[6:] + ".out", den_output)


