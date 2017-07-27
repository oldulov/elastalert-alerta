from elastalert.alerts import Alerter, BasicMatchString


from alertaclient.api import ApiClient
from alertaclient.alert import Alert

class AlertaAlerter(Alerter):

    # By setting required_options to a set of strings
    # You can ensure that the rule config file specifies all
    # of the options. Otherwise, ElastAlert will throw an exception
    # when trying to load the rule.
    # required_options = frozenset(['alerta_host', 'alerta_port', 'alerta_api_key'])
    required_options = frozenset(['alerta_endpoint', 'alerta_api_key'])

    def __init__(self, rule):
        super(AlertaAlerter, self).__init__(rule)

        # if self.rule.get('alerta_ssl'):
        #     protocol = 'https'
        # else:
        #     protocol = 'http'
        # self.endpoint = '%s://%s:%s/api' % (protocol, self.rule.get('alerta_host'), self.rule.get('alerta_port'))

        self.endpoint = self.rule.get('alerta_endpoint', None)
        self.api_key  = self.rule.get('alerta_api_key', None)

        self.event       = self.rule.get('alerta_event',       'down')
        self.severity    = self.rule.get('alerta_severity',    'warning')
        self.resource    = self.rule.get('alerta_resource',    'elastalert')
        self.environment = self.rule.get('alerta_environment', 'Development')
        self.origin      = self.rule.get('alerta_origin',      'elastalert')
        self.service     = self.rule.get('alerta_service',     ['elastalert'])
        self.text        = self.rule.get('alerta_text',        'elastalert alert')
        self.value       = self.rule.get('alerta_value',       'OK')

        self.timeout     = self.rule.get('alerta_timeout',     86400)
        self.use_match_timestamp = self.rule.get('alerta_use_match_timestamp', False)
        self.use_qk_as_resource = self.rule.get('alerta_use_qk_as_resource', False)


    # Alert is called
    def alert(self, matches):

        # Matches is a list of match dictionaries.
        # It contains more than one match when the alert has
        # the aggregation option set
#        for match in matches:

        api   = ApiClient(endpoint=self.endpoint, key=self.api_key)
        alert = Alert(resource=self.resource, event=self.event, environment=self.environment, service=self.service, severity=self.severity, text=self.text, value=self.value)

        api.send(alert)


    # get_info is called after an alert is sent to get data that is written back
    # to Elasticsearch in the field "alert_info"
    # It should return a dict of information relevant to what the alert does
    def get_info(self):
        return {'type': 'alerta',
                'alerta_url': self.url}

