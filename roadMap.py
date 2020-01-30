
from datetime import datetime
def roadmap(tasks, queries):
    rs = []
    tasksSorted = sorted(tasks, key=lambda task: (task[2], task[0]))
    for query in queries:
        p = []
        for task in tasksSorted:
            if datetime.strptime(task[1], "%Y-%m-%d") < datetime.strptime(query[1], "%Y-%m-%d") < datetime.strptime(task[2], "%Y-%m-%d") and query[0] in task[3:]:
                p.append(task[0])
        rs.append(p)
    return rs

def takeThird(elem):
    return elem[2]

print roadmap([

    ["RXGWB", "2017-10-10", "2017-12-09", "Kyle"],
    ["QOEHU", "2017-08-25", "2017-12-11", "Corey", "Kai", "Kaleb", "Reuben"],
    ["HRCPX", "2017-04-04", "2017-07-21", "Corey", "Jenson", "Kyle"],
    ["SQFYX", "2017-07-07", "2017-12-02", "Reuben", "Kaleb", "Kai", "Kyle"],
    ["BIDVM", "2017-04-20", "2017-12-08", "Kaleb"]

],
    [

        ["Reuben", "2017-06-09"],
        ["Jenson", "2017-04-13"],
        ["Corey", "2017-12-01"],
        ["Jenson", "2017-05-23"],
        ["Corey", "2017-08-19"]

    ])