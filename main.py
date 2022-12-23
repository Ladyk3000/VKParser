from Repository.UserHandler import UserHandler


def main():
    # list of users domains that you want to parse
    users_domains = ['first_domain', 'second_domain']
    handler = UserHandler()
    for user_domain in users_domains:
        handler.get_user_information(user_domain)
        handler.write_user_information()


if __name__ == '__main__':
    main()
