# elastalert-alerta

Custom Elastalert alerta Alerter module.
========================
This module is using the python alerta client (https://github.com/alerta/python-alerta-client) to send alert from elastalert to alerta.

----

Installation
------------

To install the Alerta CLI tool run:

    $ pip install alerta

According to http://elastalert.readthedocs.io/en/latest/recipes/adding_alerts.html put the modules/ directory in a location where it can be imported as a python module, e.g. under ELASTALERT_HOME.

    $ ELASTALERT_HOME=/opt/elastalert/
    $ #-> $ELASTALERT_HOME/modules


Usage
------------
To use the new Alerter, in the elastalert rule configuration file, we are going to specify the alert by writing


    $ cat rules/test.yaml
      alert:
      - "modules.alerter.alerta.AlertaAlerter"

      # @params: modules.alerta.AlertaAlerter
      alerta_endpoint: 'ALERTA_URL/api'
      alerta_api_key: 'ALERTA_API_KEY_FOR_ELASTALERT'
 
      # can be also specified
      alerta_event:      'frequency'
      alerta_severity:   'warning'
      alerta_resource:   'elastalert'
      alerta_environment: 'Production'
      alerta_origin:     'elastalert'
      alerta_service:    ['elastalert']
      alerta_text:       'Elastalert: msg_state failed'
      alerta_value:      'OK'

