def multiSelection(dimensions, tasks, mouseCoordinates):
    fi = [[0,0],[dimensions[0],dimensions[1]]]
    mFirstPoint = mouseCoordinates[0]
    mSecondPoint = mouseCoordinates[1]
    currTask = fi
    at = []
    at.append(fi)
    for i in range(len(tasks)-1):
        fc = [currTask[0][0],currTask[0][1]+dimensions[2]+dimensions[1]]
        sc = [currTask[1][0],currTask[1][1]+dimensions[2]+dimensions[1]]
        currTask = [fc,sc]
        at.append(currTask)
    at = zip(tasks,at)
    if mSecondPoint[1] < mFirstPoint[1]:
            ch = range(mSecondPoint[1],mFirstPoint[1]+1)
    else:
            ch = range(mFirstPoint[1],mSecondPoint[1] + 1)
    rl = []
    for task in at:
                    h = range(task[1][0][1],task[1][1][1] + 1)
                    if bool(set(ch) & set(h)):
                          rl.append(task[0])

    return rl

print multiSelection([200, 4, 2], ["one",
 "twoe",
 "three",
 "foure",
 "five",
 "sixe",
 "sevene"],[[170,4],
 [120,12]])