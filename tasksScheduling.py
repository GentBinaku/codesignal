def tasksScheduling(workingHours, tasks,count=0):
    fw = workingHours
    if len(tasks) == 1 and workingHours < tasks[0]:
            return  -1
    if workingHours == 0 or len(tasks) == 0:
            return count
    else:
       a = []
       for i in tasks:
           if i <= workingHours:
                a.append(i)
                count = count + 1
                workingHours = workingHours - i
                while(any(k <= workingHours for k in Diff(tasks,a))):
                        for j in tasks:
                            if j <= workingHours:
                                a.append(j)
                                workingHours = workingHours - j
                break
       return tasksScheduling(fw,tasks,count)

def Diff(li1, li2):
    for i in li2:
        for j in li1:
            if i == j:
                li1.remove(j)
                break
    return li1



print tasksScheduling(7,[1, 4, 5, 3])

