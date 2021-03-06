class User:
    '''
    Class that generates new instance of users.
    '''

    user_list = []

    def save_user(self):
        '''
        This method saves users in the user_list
        '''
        User.user_list.append(self)

    def delete_user(self):
        '''
        The method removes a saved user
        '''

        User.user_list.remove(self)

    @classmethod
    def display_user(cls):
        '''
        method that returns user user list
        '''
        return cls.user_list


    def __init__(self,first_name,last_name,password):

        self.first_name = first_name
        self.last_name = last_name
        self.password = password




class Credential:
    '''
    The class generates new instances of Credentials
    '''

    credential_list = []

    def save_credential(self):
        '''
        # 	for user in User.users_list:
        '''

        Credential.credential_list.append(self)

    @classmethod
    def display_credentials(cls):
        '''
        Method that returns credential list
        '''

        return cls.credential_list

    @classmethod
    def find_by_user_name(cls, user_name):
        '''
        Method that helps search for username and returns credential
        '''

        for credential in cls.credential_list:
            if credential.user_name == user_name:
                return credential









    def __init__(self,user_name,account_name,site,site_password):

        self.user_name = user_name
        self.account_name = account_name
        self.site = site
        self.site_password = site_password
