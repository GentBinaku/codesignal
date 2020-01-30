def smartAssigning(names, statuses, projects, tasks):
    unsorted = []
    for i in range(len(names)):
        unsorted.append([names[i], statuses[i],projects[i], tasks[i]])
    return sortFunc(unsorted)[0][0]

def sortFunc(e):
        for j in range(len(e)):
                for i in range(j+1,len(e)):
                        a = e[j]
                        b = e[i]
                        if a[1] == True or b[1] == True:
                            e[j], e[i] = e[i], e[j]
                        if a[3] < b[3] or a[3] > b[3]:
                            e[j], e[i] = e[i], e[j]
                        if a[3] == b[3]:
                            if a[2] > b[2]:
                                e[j], e[i] = e[i], e[j]
        return e

print smartAssigning(["John", "Martin", "Luke"],[False, True ,False],[1, 0, 2],[2, 0, 1])