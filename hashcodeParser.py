class human():
    def __init__(self,name:str):
        self.skills_list=list()
        self.name=name

    def __str__(self):
        return "human:%s, skills %s"%(self.name,str(self.skills_list))

class project():
    def __init__(self,name:str,time:int,score:int,best_before:int):
        self.name=name
        self.time=time
        self.score=score
        self.best_before=best_before
        self.roles=list()

    def __str__(self):
        return "project:%s, roles %s"%(self.name,str(self.roles))

def parse_file(den_file:str):
    fileke=open(den_file,'r')
    mensen=list()
    projecten=list()

    aantallen=fileke.readline()
    aantallen=aantallen.replace("\n","").split(" ")
    for iterator in range(int(aantallen[0])):
        persoon = fileke.readline().replace("\n","").split(" ")
        hm=human(persoon[0])
        for jterator in range(int(persoon[1])):
            skill=fileke.readline().replace("\n", "").split(" ")
            hm.skills_list.append((skill[0],int(skill[1])))
        mensen.append(hm)
    for iterator in range(int(aantallen[1])):
        project_string=fileke.readline().replace("\n", "").split(" ")
        pj=project(project_string[0],int(project_string[1]),int(project_string[2]),int(project_string[3]))
        for jterator in range(int(project_string[4])):
            skill=fileke.readline().replace("\n", "").split(" ")
            pj.roles.append((skill[0],int(skill[1])))
        projecten.append(pj)
    return mensen,projecten




if __name__ == '__main__':
    mensen,projecten=parse_file("input/f_find_great_mentors.in.txt")
    print()