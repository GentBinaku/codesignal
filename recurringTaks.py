import datetime
days = ['Monday','Tuesday','Wednesday','Thursday','Friday', 'Saturday','Sunday']
def recurringTask(firstDate, k, daysOfTheWeek, n):
    rd = []
    ra = []
    r = []
    fs = map(int,firstDate.split('/'))
    firstDateDateTimeObject = datetime.datetime(fs[2],fs[1],fs[0])
    for i in range(len(days)):
        c = firstDateDateTimeObject + datetime.timedelta(days=i)
        rd.append([days[c.weekday()],c])
    for i in rd:
        if i[0] in daysOfTheWeek:
           ra.append(i[1])
    for s in range(n):
            for i in range(len(ra)):
                    ra.append( + datetime.timedelta(weeks=k+s))
    for i in ra[:n]:
        r.append(i.strftime("%d/%m/%Y"))
    return r
    #if wd[firstDateDateTimeObject.weekday()]:
    #       i = firstDateDateTimeObject.weekday() + 1
    #       count = 1
    #       while True:
    #           if i >= len(wd):
    #               i = 0
    #           if wd[i] == 1:
    #               break
    #           i += 1
    #           count += 1
    #secondDateDateTimeObject = firstDateDateTimeObject.__add__(timedelta(days=count))
    #d.append(firstDateDateTimeObject.date())
    #rd.append(secondDateDateTimeObject.date())
    #for i in range(n):
    #       rd.append(firstDateDateTimeObject.__add__(timedelta(weeks=k+i)))
    #       rd.append(secondDateDateTimeObject.__add__(timedelta(weeks=k + i)))
    #return rd[:n]


print recurringTask("30/05/1995",4,["Tuesday"],1)