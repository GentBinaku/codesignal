def launchSequenceChecker(systemNames, stepNumbers):
    d = []
    s = {}
    for i in range(len(systemNames)):
        if systemNames[i] in d:
            s[systemNames[i]].append(stepNumbers[i])
        else:
            s[systemNames[i]] = [stepNumbers[i]]
            d.append(systemNames[i])
    for v in s.values():
            if len(set(v)) != len(v):
                return False
            elif sorted(v) == v:
                return True
            else:
                return False






print launchSequenceChecker(["Falcon 9",
 "Falcon 9",
 "Falcon 9",
 "Falcon 9",
 "Falcon 9",
 "Falcon 9"],[1, 3, 5, 7, 7, 9])