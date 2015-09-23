import time
from pnc_cli import utils
from pnc_cli.swagger_client.apis.buildconfigurations_api import BuildconfigurationsApi
from pnc_cli.swagger_client.apis.runningbuildrecords_api import RunningbuildrecordsApi

configs_api = BuildconfigurationsApi(utils.get_api_client())
running_api = RunningbuildrecordsApi(utils.get_api_client())


def test_get_all():
    # start a build so that a build is running
    configs_api.trigger(id=1)
    running_builds = running_api.get_all().content
    time.sleep(5)
    assert running_builds is not None


def test_get_specific():
    configs_api.trigger(id=1)
    running_build = running_api.get_specific(id=1)
    time.sleep(5)
    assert running_build is not None
