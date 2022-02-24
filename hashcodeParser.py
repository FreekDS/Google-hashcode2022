import logic
import output

class human():
    def __init__(self,name:str):
        self.skills_list=list()
        self.name=name
    def get_skill(self,sk:str):
        for i in self.skills_list:
            if(i[0]==sk):
                return i
        return None
    def increment_skill(self,sk,amount):
        for i in self.skills_list:
            if(i[0]==sk and i[1]<=amount):
                i[1]+=1
                return

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
            hm.skills_list.append([skill[0],int(skill[1])])
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
  #  mensen,projecten=parse_file("input/a_an_example.in.txt")
  #  mensen, projecten = parse_file('input/b_better_start_small.in.txt')
  #  mensen,projecten=parse_file('input/c_collaboration.in.txt')
  #  mensen, projecten = parse_file('input/d_dense_schedule.in.txt')
  #  mensen, projecten = parse_file('input/e_exceptional_skills.in.txt')
    mensen, projecten = parse_file('input/f_find_great_mentors.in.txt')

    succ = logic.calc_order(mensen, projecten)
    output.write_output_maar_dan_goed("output/F.txt", succ)
    print()