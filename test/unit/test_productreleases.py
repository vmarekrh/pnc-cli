__author__ = 'thauser'
from mock import patch, MagicMock
from pnc_cli import productreleases
from pnc_cli.swagger_client.models import ProductReleaseRest


def test_create_product_release_object():
    compare = ProductReleaseRest()
    compare.version = '1.0.1.DR1'
    compare.support_level = 'EOL'
    result = productreleases.create_product_release_object(version='1.0.1.DR1', support_level='EOL')
    assert result.to_dict() == compare.to_dict()


@patch('pnc_cli.productreleases.releases_api.get_all', return_value=MagicMock(content='list of all releases'))
def test_list_product_releases(mock):
    result = productreleases.list_product_releases()
    mock.assert_called_once_with(page_size=200, sort='', q='')
    assert result == 'list of all releases'


@patch('pnc_cli.productreleases.create_product_release_object')
@patch('pnc_cli.productreleases.releases_api.create_new')
@patch('pnc_cli.productreleases.productversions_api.get_specific')
def test_create_release_badversion(mock_get_specific, mock_create_new, mock_create_object):
    result = productreleases.create_release(version='x.x')
    assert not mock_create_object.called
    assert not mock_create_new.called
    assert not mock_get_specific.called
    assert not result


@patch('pnc_cli.productreleases.create_product_release_object', return_value='created release')
@patch('pnc_cli.productreleases.releases_api.create_new', return_value=MagicMock(content='created release'))
@patch('pnc_cli.productreleases.productversions_api.get_specific',
       return_value=MagicMock(content=MagicMock(version='1.0')))
def test_create_release(mock_get_specific, mock_create_new, mock_create_object):
    result = productreleases.create_release(version='0.DR1',
                                            release_date='2016-01-01',
                                            download_url='https://tom.com',
                                            product_version_id=1,
                                            product_milestone_id=1,
                                            support_level='EOL')
    mock_get_specific.assert_called_once_with(id=1)
    mock_create_new.assert_called_once_with(body='created release')
    mock_create_object.assert_called_once_with(version='1.0.0.DR1',
                                               release_date='2016-01-01',
                                               download_url='https://tom.com',
                                               product_version_id=1,
                                               product_milestone_id=1,
                                               support_level='EOL')
    assert result == 'created release'


@patch('pnc_cli.productreleases.releases_api.get_all_by_product_version_id',
       return_value=MagicMock(content='list of releases for version'))
def test_list_releases_for_version(mock):
    result = productreleases.list_releases_for_version(1)
    mock.assert_called_once_with(version_id=1)
    assert result == 'list of releases for version'


@patch('pnc_cli.productreleases.releases_api.get_specific', return_value=MagicMock(content='single release'))
def test_get_release(mock):
    result = productreleases.get_release(1)
    mock.assert_called_once_with(id=1)
    assert result == 'single release'


@patch('pnc_cli.productreleases.releases_api.get_all',
       return_value=MagicMock(content=[MagicMock(id=1), MagicMock(id=2)]))
def test_product_release_exists(mock):
    result = productreleases._product_release_exists(1)
    mock.assert_called_once_with()
    assert result


@patch('pnc_cli.productreleases._product_release_exists', return_value=False)
@patch('pnc_cli.productreleases.releases_api.get_specific')
@patch('pnc_cli.productreleases.releases_api.update')
def test_update_release_notexist(mock_update, mock_get_specific, mock_release_exists):
    result = productreleases.update_release(1)
    mock_release_exists.assert_called_once_with(1)
    assert not mock_get_specific.called
    assert not mock_update.called


@patch('pnc_cli.productreleases._product_release_exists', return_value=True)
@patch('pnc_cli.productreleases.releases_api.get_specific')
@patch('pnc_cli.productreleases.releases_api.update', return_value=MagicMock(content='updated release'))
def test_update_release(mock_update, mock_get_specific, mock_release_exists):
    mock = MagicMock()
    mockcontent = MagicMock(content=mock)
    mock_get_specific.return_value = mockcontent
    result = productreleases.update_release(id=1, version='2.2.2.GA', support_level='EOL')
    mock_release_exists.assert_called_once_with(1)
    assert getattr(mock, 'version') == '2.2.2.GA'
    assert getattr(mock, 'support_level') == 'EOL'
    mock_update.assert_called_once_with(id=1, body=mock)
    assert result == 'updated release'
