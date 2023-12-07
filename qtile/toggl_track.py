from libqtile.widget import base
import requests
from base64 import b64encode

import json

API_TOKEN = 'cd2616be43b8f73be4d736b27a1b2fba'

def get_current_time_entry():
    data = requests.get(
            'https://api.track.toggl.com/api/v9/me/time_entries/current',
            headers = {
                'content-type': 'application/json',
                'Authorization' : 'Basic %s' %  b64encode(API_TOKEN.encode() + b":api_token").decode("ascii")
        })
    return data.json()

def get_project_name(time_entry):
    project_id = time_entry['project_id']
    if not project_id: return 'No Project'
    workspace_id = time_entry['workspace_id']
    data = requests.get(
            f'https://api.track.toggl.com/api/v9/workspaces/{workspace_id}/projects/{project_id}',
            headers={
                'content-type': 'application/json',
                'Authorization' : 'Basic %s' %  b64encode(API_TOKEN.encode() + b":api_token").decode("ascii")
        })
    return data.json()['name']

class TogglTrack(base.InLoopPollText):

    defaults = [
        ("update_interval", 5.0, "Update interval for the TogglTrack widget"),
    ]

    def __init__(self, **config):
        super().__init__("", **config)
        self.add_defaults(TogglTrack.defaults)

    def poll(self) -> str:
        time_entry = get_current_time_entry()
        if not time_entry: return "Not Tracking"
        description = time_entry['description']
        project = get_project_name(time_entry)
        return f"{description} [{project}]"
