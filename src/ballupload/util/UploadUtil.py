import json
import logging
import requests
from ballupload.resources.properties import Properties


class BallchasingApi(object):
    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.log.setLevel(logging.INFO)

    def create_group(self, name, player_id, team_id, parent=None):
        payload = {"name": name, "player_identification": player_id,
                   "team_identification": team_id} if parent is None else {"name": name, "parent": parent,
                                                                           "player_identification": player_id,
                                                                           "team_identification": team_id}
        payload = json.dumps(payload)
        r = requests.post('https://ballchasing.com/api/groups', headers=Properties().headers, data=payload)
        if r.status_code == 201:
            js = r.json()
            self.log.info(f'Created Group: {js["id"]}')
            return js['id']
        else:
            r.raise_for_status()

    def upload_replay(self, replay, group_id):
        files = {'file': open(replay, 'rb')}
        url = 'https://ballchasing.com/api/v2/upload?visibility=public&group=' + group_id
        r = requests.post(url, headers=Properties().headers, files=files)
        print(r.json())
        if r.status_code == 201:
            res = r.json()
            self.log.info(f'Uploaded Replay: {res["id"]}')
            return res['id']
        elif r.status_code == 409:
            res = r.json()
            self.log.warning(f'Duplicate Replay: {res["id"]}')
            patching = self.patch_replay(res['id'], group_id)
            if patching is True:
                return res['id']
            else:
                self.log.error("Error Patching Replays")
                raise Exception
        else:
            self.log.error("Error Uploading Replays")
            r.raise_for_status()

    def patch_replay(self, replay_id, group_id):
        payload = {"group": group_id}
        url = 'https://ballchasing.com/api/replays/{}'.format(replay_id)
        r = requests.patch(url, headers=Properties().headers, json=payload)
        if r.status_code == 204:
            return True

    def get_group(self, group_id):
        url = 'https://ballchasing.com/api/groups/{}'.format(group_id)
        while True:
            r = requests.get(url, headers=Properties().headers)
            if r.status_code == 200:
                js = r.json()
                if js['status'].lower() == 'ok':
                    return js
            else:
                r.raise_for_status()
