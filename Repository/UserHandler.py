import os
import json

from Parser import Parser
import config


class UserHandler:
    def __init__(self):
        self.user_id = None
        self.user_info = None
        self.user_subs = None
        self.user_group_names = None
        self.user_subscribers_names = None
        self.user_wall_posts =None
        self.data_directory = 'UsersData'
        self.parser = Parser()

    def get_user_information(self, user_id):
        self.user_id = user_id
        user_fields = ','.join(field for field in config.fields)
        self.user_info = self.parser.get_user_info(self.user_id, user_fields)

        self.user_subs = self.parser.get_user_subs(self.user_id)
        user_groups = ','.join(str(group) for group in self.user_subs['response']['groups']['items'])
        self.user_group_names = self.parser.get_group_names(user_groups)

        user_subscribers = ','.join(str(group) for group in self.user_subs['response']['users']['items'])
        self.user_subscribers_names = self.parser.get_group_names(user_subscribers)

        self.user_wall_posts = self.parser.get_user_wall_posts(self.user_id)

    def write_user_information(self):
        if os.path.exists(f'{self.data_directory}/user_{self.user_id}'):
            pass
        else:
            os.mkdir(f'{self.data_directory}/user_{self.user_id}')

        with open(f'{self.data_directory}/user_{self.user_id}/info_{self.user_id}.json', 'w', encoding="utf-8") as file:
            json.dump(self.user_info, file, indent=4, ensure_ascii=False)

        with open(f'{self.data_directory}/user_{self.user_id}/subs_{self.user_id}.json', 'w', encoding="utf-8") as file:
            json.dump(self.user_subs, file, indent=4, ensure_ascii=False)

        with open(f'{self.data_directory}/user_{self.user_id}/group_names_{self.user_id}.json', 'w', encoding="utf-8") as file:
            json.dump(self.user_group_names, file, indent=4, ensure_ascii=False)

        with open(f'{self.data_directory}/user_{self.user_id}/subscribers_names_{self.user_id}.json', 'w', encoding="utf-8") as file:
            json.dump(self.user_subscribers_names, file, indent=4, ensure_ascii=False)

        with open(f'{self.data_directory}/user_{self.user_id}/user_wall_posts_{self.user_id}.json', 'w', encoding="utf-8") as file:
            json.dump(self.user_wall_posts, file, indent=4, ensure_ascii=False)