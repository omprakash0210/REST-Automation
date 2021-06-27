"""
This script will be used to start the test
by making http calls from local VMs
"""

import os
import yaml
import requests
from requests.exceptions import InvalidURL
from prettytable import PrettyTable


def api_calls(apis):
    """

    :param apis: list of APIs added in the Project_config.yaml file
    :return: prints tabular report of APIs testing
    """
    comments = 'No Comments'

    user_agent = {'User-agent': 'Mozilla/89.0.2 (X11; '
                                'Linux x86_64) Chrome/91.0.4472.114'}  # user agent simulate
    # different browser

    report_header = PrettyTable(
        ["API Name", "URLs", "Method Type", "Expected Response Code", "Actual Response Code",
         "Pass/Fail", "Remarks"])

    try:
        for api in apis:

            req = requests.get(api['url'], headers=user_agent)

            if req.status_code == 200:
                report_header.add_row(
                    [api['api_name'], api['url'], api['method_type'], api['expected_response_code'],
                     req.status_code, "PASS", comments])

            else:
                comments = 'Expected Response code {0} but actual response code {1}'.format(
                    api['expected_response_code'], req.status_code)

                report_header.add_row(
                    [api['api_name'], api['url'], api['method_type'], api['expected_response_code'],
                     req.status_code, "Failed", comments])

    except InvalidURL as url_exception:  # In-case of Invalid end-points. Raise exceptions
        print url_exception

    print report_header


def individual_apis(api_name):
    """
    :param api_name: get the API name and match with config yaml. Returns all key-value of yaml
    :return:
    """

    src = os.path.abspath(os.path.dirname(__file__))
    config = os.path.join(src, 'config', 'Project_config.yaml')

    with open(config, 'r') as api_info:
        try:
            data = yaml.safe_load(api_info)
            for api in data:
                if api_name == api['api_name']:
                    api_calls([api])
                else:
                    print 'Please confirm the APIs name'

        except Exception as exp:
            print 'Unexpected Exception occurred', exp
