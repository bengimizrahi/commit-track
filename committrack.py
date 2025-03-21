from datetime import datetime, date
import pytest
import pprint
import pdb
class Resource:
    def __init__(self, name, internal=True):
        self.name = name
        self.internal = internal

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, rhs):
        return isinstance(rhs, self.__class__) and (self.name == rhs.name)
    
    def __repr__(self):
        return pprint.pformat(f"{self.__class__.__name__}({self.__dict__})")

class Task:
    def __init__(self, identifier, description, person, duration):
        self.identifier = identifier
        self.description = description
        self.person = person
        self.duration = duration
    
    def __hash__(self):
        return hash(self.identifier)

    def __eq__(self, rhs):
        return isinstance(rhs, self.__class__) and (self.identifier == rhs.identifier)

    def __repr__(self):
        return pprint.pformat(f"{self.__class__.__name__}({self.__dict__})")

class Effort:
    def __init__(self, date, person, task, duration):
        self.date = date
        self.person = person
        self.task = task
        self.duration = duration
    
    def __eq__(self, rhs):
        return isinstance(rhs, self.__class__) and (vars(self) == vars(rhs))

    def __repr__(self):
        return pprint.pformat(f"{self.__class__.__name__}({self.__dict__})")

class Project:
    def __init__(self):
        self.resources : dict[str, Resource] = dict()
        self.tasks : dict[str, Task] = dict()
        self.efforts : list[Effort] = []
        # states
        self.currentDay = None

    def __repr__(self):
        return pprint.pformat(f"{self.__class__.__name__}({self.__dict__})")

    def addResource(self, person):
        if person in self.resources:
            return False
        self.resources[person] = Resource(person)
        return True
    
    def addTask(self, identifier, description=None, person=None, duration=0):
        if identifier in self.tasks:
            return False
        self.tasks[identifier] = Task(identifier, description, person, duration)
        return True

    def addEffort(self, date, person, task, duration):
        self.efforts.append(Effort(date, person, task, duration))

    def __firstDate__(self):
        if len(self.efforts) == 0:
            return None
        firstDate = min((w.date for w in self.efforts))
        return firstDate

    def __sortedEfforts__(self):
        efforts = sorted(self.efforts, key=lambda w: w.date)
        return efforts
    
    def generateReport(self):
        class Report:
            class TaskStatus:
                def __init__(self):
                    self.daysSpent = 0.0

                def __repr__(self):
                    return pprint.pformat(f"{self.__class__.__name__}({self.__dict__})")

                def logEffort(self, duration):
                    self.daysSpent += duration

            def __init__(self, resources, tasks):
                self.resources : dict[str, Resource] = resources
                self.tasks : dict[str, Task] = tasks
                self.worklogs : dict[Resource, dict[date, list[Effort]]] = dict()
                self.taskStatuses : dict[Task, Report.TaskStatus] = dict()
                for r in self.resources.values():
                    self.worklogs[r] = dict()
            
            def __repr__(self):
                return pprint.pformat(f"{self.__class__.__name__}({self.__dict__})")

            def __updateWorklog__(self, effort):
                resource = self.resources[effort.person]
                worklog = self.worklogs[resource]
                efforts = worklog.setdefault(effort.date, [])
                efforts.append(effort)

            def __updateTaskStatus__(self, effort):
                task = self.tasks[effort.task]
                taskStatus = self.taskStatuses.setdefault(task, Report.TaskStatus())
                taskStatus.logEffort(effort.duration)

            def processEfforts(self, efforts: list[Effort]):
                for e in efforts:
                    self.__updateWorklog__(e)
                    self.__updateTaskStatus__(e)
        
        report = Report(self.resources, self.tasks)
        report.processEfforts(self.efforts);
        return report