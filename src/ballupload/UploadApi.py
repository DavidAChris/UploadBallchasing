import os
from os import listdir
from os.path import isfile, join
from resources.properties import Properties
from service.UploadService import GameSubmit


def upload_handler():
    props = Properties()
    replay_files = [f for f in listdir(props.replay_download) if isfile(join(props.replay_download, f))]
    group_name = input("Group Name: ")
    while True:
        season = int(input("Which Season?\n1) Pre\n2) Reg\n3) Playoffs\nPlease Choose One: "))
        if season == 1:
            games = GameSubmit(group_name, replay_files, props.pre_season)
            games.create_group()
            games.download_replays()
            break
        elif season == 2:
            games = GameSubmit(group_name, replay_files, props.reg_Season)
            games.create_group()
            games.download_replays()
            break
        elif season == 3:
            games = GameSubmit(group_name, replay_files, props.playoffs)
            games.create_group()
            games.download_replays()
            break
    print(f'https://ballchasing.com/group/{games.group_id}')
    for file in replay_files:
        os.remove(os.path.join(props.replay_download, file))
