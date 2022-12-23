import requests
from collections import OrderedDict
from access import token
import config


class Parser:
    def __init__(self):
        self.base_url = 'https://api.vk.com/method/'
        self.params_dict = OrderedDict([('user_ids', None),
                                        ('fields', None),
                                        ('access_token', token),
                                        ('v', config.api_version)])

    def get_user_info(self, user_id, fields):
        self.params_dict['user_ids'] = user_id
        self.params_dict['fields'] = fields
        url = f"{self.base_url}users.get"
        try:
            response = requests.get(url, params=self.params_dict)
            return response.json()
        except:
            print('smth wrong with http request to get user info')

    def get_user_subs(self, user_id):
        self.params_dict = OrderedDict([('user_id', user_id),
                                        ('access_token', token),
                                        ('v', config.api_version)])
        url = f"{self.base_url}users.getSubscriptions"
        try:
            response = requests.get(url, params=self.params_dict)
            return response.json()
        except:
            print('smth wrong with http request to get user subs')

    def get_group_names(self, group_id):
        self.params_dict = OrderedDict([('group_ids', group_id),
                                        ('access_token', token),
                                        ('v', config.api_version)])
        url = f"{self.base_url}groups.getById"
        try:
            response = requests.get(url, params=self.params_dict)
            return response.json()
        except:
            print('smth wrong with http request to get group names')

    def get_user_wall_posts(self, user_id):
        self.params_dict = OrderedDict([('owner_id', user_id),
                                        ('access_token', token),
                                        ('v', config.api_version)])
        url = f"{self.base_url}wall.get"
        try:
            response = requests.get(url, params=self.params_dict)
            return response.json()
        except:
            print('smth wrong with http request to get user wall posts')

