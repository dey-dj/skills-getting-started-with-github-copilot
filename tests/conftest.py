from copy import deepcopy

import pytest

from src import app


@pytest.fixture
def isolated_activities():
    original_activities = deepcopy(app.activities)

    yield app.activities

    app.activities.clear()
    app.activities.update(original_activities)
