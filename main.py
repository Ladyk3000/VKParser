from Repository.UserHandler import UserHandler


def main():
    users_ids = ['62860']
    handler = UserHandler()
    for user_id in users_ids:
        handler.get_user_information(user_id)
        handler.write_user_information()


if __name__ == '__main__':
    main()
