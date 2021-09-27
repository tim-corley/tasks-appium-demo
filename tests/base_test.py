import pytest


@pytest.mark.usefixtures("setup")
class BaseTest:
    pass


@pytest.mark.usefixtures("setup", "blank_list")
class BlankListStartTest:
    pass


@pytest.mark.usefixtures("setup", "blank_list", "sample_list")
class SampleListStartTest:
    pass