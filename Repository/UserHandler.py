import os
import json

from Repository.Parser import Parser
import config


class UserHandler:
    def __init__(self):
        self.user_domain = None
        self.user_info = None
        self.user_subs = None
        self.user_group_names = None
        self.user_subscribers_names = None
        self.user_wall_posts = None
        self.file_directory = 'UsersData'
        self.user_directory = f'{self.file_directory}/{self.user_domain}'
        self.parser = Parser()


    def get_user_information(self, user_domain):
        self.user_domain = user_domain

        user_fields = ','.join(field for field in config.fields)
        self.user_info = self.parser.get_user_info(self.user_domain, user_fields)

        if not self.user_info['response'][-1]['is_closed']:
            user_id = self.user_info['response'][0]['id']
            self.user_subs = self.parser.get_user_subs(user_id)

            user_groups = ','.join(str(group) for group in self.user_subs['response']['groups']['items'])
            self.user_group_names = self.parser.get_group_names(user_groups)

            user_subscribers = ','.join(str(group) for group in self.user_subs['response']['users']['items'])
            self.user_subscribers_names = self.parser.get_group_names(user_subscribers)

            self.user_wall_posts = self.parser.get_user_wall_posts(user_id)

    def write_user_information(self):

        if os.path.exists(self.file_directory):
            pass
        else:
            os.mkdir(self.file_directory)

        self.user_directory = f'{self.file_directory}/{self.user_domain}'
        if os.path.exists(self.user_directory):
            pass
        else:
            os.mkdir(self.user_directory)

        with open(f'{self.user_directory}/user_info_{self.user_domain}.json', 'w', encoding="utf-8") as file:
            json.dump(self.user_info, file, indent=4, ensure_ascii=False)

        if not self.user_info['response'][-1]['is_closed']:

            with open(f'{self.user_directory}/subs_{self.user_domain}.json', 'w', encoding="utf-8") as file:
                json.dump(self.user_subs, file, indent=4, ensure_ascii=False)

            with open(f'{self.user_directory}/group_names_{self.user_domain}.json', 'w', encoding="utf-8") as file:
                json.dump(self.user_group_names, file, indent=4, ensure_ascii=False)

            with open(f'{self.user_directory}/subscribers_names_{self.user_domain}.json', 'w', encoding="utf-8") as file:
                json.dump(self.user_subscribers_names, file, indent=4, ensure_ascii=False)

            with open(f'{self.user_directory}/user_wall_posts_{self.user_domain}.json', 'w', encoding="utf-8") as file:
                json.dump(self.user_wall_posts, file, indent=4, ensure_ascii=False)

