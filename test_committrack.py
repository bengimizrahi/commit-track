import pytest
from datetime import date
import committrack
import pprint

@pytest.fixture
def emptyProject():
    return committrack.Project()

def test_firstDateNotDetermined(emptyProject):
    assert emptyProject.__firstDate__() == None

@pytest.fixture
def sampleProjectWithMinimalEffort():
    project = committrack.Project()
    project.addEffort(date(2025, 10, 1), "Bengi Mizrahi", "Task-1", 1)
    project.addEffort(date(2025, 10, 2), "Bengi Mizrahi", "Task-2", 1)
    project.addEffort(date(2025, 10, 3), "Bengi Mizrahi", "Task-1", 1)
    return project

def test_memfn_firstDate(sampleProjectWithMinimalEffort):
    assert sampleProjectWithMinimalEffort.__firstDate__() == date(2025, 10, 1)

@pytest.fixture
def sampleProjectWithNonChronogicalEfforts():
    project = committrack.Project()
    project.addEffort(date(2025, 10, 2), "Bengi Mizrahi", "Task-2", 1)
    project.addEffort(date(2025, 10, 1), "Bengi Mizrahi", "Task-1", 1)
    return project

def test_memfn_sortedEfforts(sampleProjectWithNonChronogicalEfforts):
    assert sampleProjectWithNonChronogicalEfforts.__sortedEfforts__() == [
        committrack.Effort(date(2025, 10, 1), "Bengi Mizrahi", "Task-1", 1),
        committrack.Effort(date(2025, 10, 2), "Bengi Mizrahi", "Task-2", 1)
    ]

@pytest.fixture
def minimalMeaningfulProject():
    project = committrack.Project()
    project.addTask("1", "Task one", "Bengi Mizrahi", 1)
    pprint.pprint(vars(project))
    return project

def test_report(minimalMeaningfulProject):
    pprint.pprint(vars(minimalMeaningfulProject))
    report = minimalMeaningfulProject.generateReport()
    pprint.pprint(vars(report))