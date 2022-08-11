from random import shuffle

class EmployeeMatch:
    def __init__(self, names=[]):
        self.names = names
        self.matchHistory  = set()
        self.allMatched = False

    def matchEmployees(self):
        if self.allMatched:
            return "Get some more employees in the list, everyone has been matched"
        # declare a list of employees, noting that none have matched
        matched = {}
        for name in self.names:
            matched[name] = False

        # match employees
        employeeMatches = []
        shuffle(self.names)
        for e1 in self.names:
            for e2 in self.names:
                if e1 is not e2 and not matched[e1] and not matched[e2] and (e1,e2) not in self.matchHistory:
                    employeeMatches.append((e1, e2))
                    matched[e1], matched[e2] = True, True

                    for pair in [(e1,e2),(e2,e1)]:
                        self.matchHistory.add(pair) 
        
        if not employeeMatches:
            self.allMatched = True
            return "Everybody has already been matched at this point."
        return employeeMatches
    
    def addEmployee(self, name):
        self.allMatched = False
        self.names.append(name)
    
    def removeEmployee(self, name):
        del self.names[self.names.index(name)]

matcher = EmployeeMatch(['Bob', 'Brian', 'Josh', 'Joe', 'Jim'])
print(matcher.matchEmployees())
matcher.removeEmployee('Bob')
print(matcher.matchEmployees())
print(matcher.matchEmployees())
print(matcher.matchEmployees())
print(matcher.matchEmployees())
print(matcher.matchEmployees())
print(matcher.matchEmployees())
print(matcher.matchEmployees())
matcher.addEmployee("Xanthium")
print(matcher.matchEmployees())
print(matcher.matchEmployees())
print(matcher.matchEmployees())
print(matcher.matchEmployees())
print(matcher.matchEmployees())
print(matcher.matchEmployees())