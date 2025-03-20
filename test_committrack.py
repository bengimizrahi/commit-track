import pytest
from datetime import date
import committrack

@pytest.fixture
def sampleProjectWithMinimalWorklog():
    project = committrack.Project()
    project.addWorklog(date(2025, 10, 1), "Bengi Mizrahi", "Task-1", 1)
    project.addWorklog(date(2025, 10, 2), "Bengi Mizrahi", "Task-2", 1)
    project.addWorklog(date(2025, 10, 3), "Bengi Mizrahi", "Task-1", 1)
    return project

def test_firstdate(sampleProjectWithMinimalWorklog):
    assert sampleProjectWithMinimalWorklog.__firstDate__() == (date(2025, 10, 1), "Ok")
    