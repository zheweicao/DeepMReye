import os
import pytest
from pathlib import Path

@pytest.fixture
def path_to_masks():
    path = str(Path(__file__).parents[0].parents[0]) + os.path.sep + 'deepmreye/masks/'
    return path

@pytest.fixture
def path_to_participant():
    path = str(Path(__file__).parents[0]) + os.path.sep + 'data/test_participant.nii'
    return path