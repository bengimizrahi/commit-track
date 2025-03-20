import yaml
import datetime
import pytest

class Resource:
    def __init__(self, name, internal=True):
        self.name = name
        self.internal = internal

class Task:
    def __init__(self, identifier, description, person, duration):
        self.identifier = identifier
        self.description = description
        self.person = person
        self.duration = duration

class Worklog:
    def __init__(self, date, person, task, duration):
        self.date = date
        self.task = task
        self.person = person
        self.duration = duration

class Project:
    def __init__(self):
        self.resources = dict()
        self.tasks = dict()
        self.worklogs = []
        # states
        self.currentDay = 0

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

    def addWorklog(self, date, person, task, duration):
        self.worklogs.append(Worklog(date, person, task, duration))

    def __firstDate__(self):
        if len(self.worklogs) == 0:
            return (False, "Cannot determine the first date, no worklogs available")
        firstDate = min((w.date for w in self.worklogs))
        return (firstDate, "Ok")

