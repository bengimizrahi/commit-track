import yaml
from datetime import datetime, date
import pytest

class Resource:
    def __init__(self, name, internal=True):
        self.name = name
        self.internal = internal

    def __hash__(self):
        return hash(self.name)
class Task:
    def __init__(self, identifier, description, person, duration):
        self.identifier = identifier
        self.description = description
        self.person = person
        self.duration = duration

class Effort:
    def __init__(self, date, person, task, duration):
        self.date = date
        self.person = person
        self.task = task
        self.duration = duration
    
    def __eq__(self, rhs):
        return vars(self) == vars(rhs)

class Project:
    def __init__(self):
        self.resources : dict[str, Resource]= dict()
        self.tasks : dict[int, Task] = dict()
        self.efforts : list[Effort] = []
        # states
        self.currentDay = None

    def addResource(self, person):
        if person not in self.resources:
            return (False, "Duplicate resource")
        self.resources[person] = Resource(person)
        return (True, "Ok")
    
    def addTask(self, identifier, description=None, person=None, duration=0):
        if identifier not in self.tasks:
            return (False, "Duplicate task")
        self.tasks[identifier] = Task(identifier, description, person, duration)
        return (True, "Ok")

    def addEfforts(self, date, person, task, duration):
        self.efforts.append(Effort(date, person, task, duration))

    def __firstDate__(self):
        if len(self.efforts) == 0:
            return None
        firstDate = min((w.date for w in self.efforts))
        return firstDate

    def __sortedEfforts__(self):
        efforts = sorted(self.efforts, key=lambda w: w.date)
        return efforts
    
    def render(self):
        class Sheet:
            class Worklog:
                def __init__(self, firstDay, resources, tasks):
                    self.firstDay = firstDay
                    self.worklogs : dict[Resource, dict[date, list[Effort]]] = dict()

            
        if (firstDay := self.__firstDate__()) == None:
            firstDay = datetime.today()
        sheet = Sheet(firstDay, self.resources, self.tasks)
        efforts = self.__sortedEfforts__()
        for e in efforts:
