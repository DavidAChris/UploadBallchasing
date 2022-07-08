from ballupload.resources.properties import Properties
from ballupload.util.UploadUtil import BallchasingApi
import logging


class GameSubmit(object):
    def __init__(self, group, replays, parent):
        self.log = logging.getLogger(__name__)
        self.log.setLevel(logging.INFO)
        self.api = BallchasingApi()
        self.properties = Properties()
        self.parent = parent
        self.replay_id = None
        self.group_id = None
        self.group_name = group
        self.group_path = self.properties.group_path
        self.replays = replays

    def create_group(self):
        outcome = self.api.create_group(self.group_name, self.properties.player_ident, self.properties.team_ident,
                                        parent=self.parent)
        self.group_id = outcome

    def download_replays(self):
        for i in range(len(self.replays)):
            if self.replays[i] is not None:
                replay_path = f'{self.properties.replay_download}/{self.replays[i]}'
                self.api.upload_replay(replay_path, self.group_id)
