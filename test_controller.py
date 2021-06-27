"""
This script will be used to take input from user as option.
And perform action based on selection
"""
import os
import time
import yaml
import inquirer
import start_test


def get_apis(api_data):
    """
    :param api_data: pull key-value pair from config yaml file
    :return: dict of individual apis
    """
    src = os.path.abspath(os.path.dirname(__file__))
    config = os.path.join(src, 'config', api_data + '.yaml')

    with open(config, 'r') as api_info:
        try:
            data = yaml.safe_load(api_info)
            return data # return the config data as object

        except yaml.YAMLError as exc:
            print exc


if __name__ == '__main__':
    """
    :param DOCKER_SETUP: enable docker container
    EXEC_SETUP: Choose whole run or individual APIs (wisely option)
    API_SETUP: return individual API test run.
    """

    API_DATA = 'Project_config'

    # Input from user
    DOCKER_SETUP = [
        inquirer.List(
            "selection",
            message="Do you want to initialize Docker container? We are setting up Ngnix container",
            choices=["Yes", "No"],
        ),
    ]

    EXEC_SETUP = [
        inquirer.List(
            "selection",
            message="Do you want to test All APIs",
            choices=["Yes", "No"],
        ),
    ]

    DOCKER_SETUP_ANS = inquirer.prompt(DOCKER_SETUP)
    EXEC_ANS = inquirer.prompt(EXEC_SETUP)

    if DOCKER_SETUP_ANS['selection'] == "Yes":
        os.system("sh setup_prerequisites/executor.sh")
    else:
        print '!!! Execution will be started based on your selection !!!'

    if EXEC_ANS['selection'] == "Yes":
        print 'Execution will be started for all APIs in Configuration'

        APIS = get_apis(API_DATA)

        time.sleep(20)
        start_test.api_calls(APIS)

    elif EXEC_ANS['selection'] == "No":

        API_SETUP = [
            inquirer.List(
                "selection",
                message="Please choose APIs you want to test",
                choices=["Launch", "Login"],
            ),
        ]

        API_ANS = inquirer.prompt(API_SETUP)

        if API_ANS['selection'] == "Launch":
            start_test.individual_apis(API_ANS['selection'])

        elif API_ANS['selection'] == "Login":
            start_test.individual_apis(API_ANS['selection'])

    CLEAN_UP = [
        inquirer.List(
            "selection",
            message="Do you want to clean up the Infrastructure Footprint",
            choices=["Yes", "No"],
        ),
    ]

    CLEANUP_ANS = inquirer.prompt(CLEAN_UP)
    if CLEANUP_ANS['selection'] == 'Yes':
        os.system('sh cleanup_footprints/cleanup.sh')
        print 'Image has been removed from the system'
    else:
        pass
