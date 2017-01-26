import logging

import iniparse.configparser as configparser

class KeycloakConfig():
    def __init__(self, config):
        self.parse_client_id(config)
        self.parse_realm(config)
        self.parse_url(config)

    def __getstate__(self):
        # things that need to be pickled here
        pass

    def __setstate__(self):
        # how to restore pickling here
        pass

    def parse_url(self, config):
        try:
            url = config.get('PNC', 'keycloakUrl')
        except configparser.noOptionError:
            logging.error('No authentication server defined. Define "keycloakUrl" in pnc-cli.conf')
            return
        self.url = url + '/auth/realms/' + self.realm + '/protocol/openid-connect/token'

    def parse_client_id(self, config):
        try:
            client_id = config.get('PNC', 'keycloakClientId')
        except configparser.NoOptionError:
            logging.error('client_id is missing for the keycloak payload. Define "keycloakClientId" in pnc-cli.conf for authentication.')
            return
        self.client_id = client_id


    def parse_realm(self, config):
        try:
            realm = config.get('PNC', 'keycloakRealm')
        except configparser.NoOptionError:
            logging.error('No keycloak authentication realm defined. Define "keycloakRealm" in pnc-cli.conf to enable authentication.')
            return
        self.realm = realm