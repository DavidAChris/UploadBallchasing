import os
import yaml


class Properties:
    def __init__(self):
        with open(os.getenv('CONFIGS')) as f:
            self.configs = yaml.safe_load(f)
        self.replay_download = self.configs['Ballchasing']['Replay_Download_Path']
        self.group_path = self.configs['Ballchasing']['Group_Path']
        self.pre_season = self.configs['Ballchasing']['Pre_Season']
        self.reg_Season = self.configs['Ballchasing']['Reg_Season']
        self.playoffs = self.configs['Ballchasing']['Playoffs']
        self.team_ident = self.configs['Ballchasing']['Team_Identification']
        self.player_ident = self.configs['Ballchasing']['Player_Identification']
        self.replay_call = self.configs['Ballchasing']['Replay_Call']
        self.headers = self.configs['Ballchasing']['headers']
