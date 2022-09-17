import requests

class VkUser:

    url = 'https://api.vk.com/method/'
    def __init__(self,token,version,id):
        self.token = token
        self.version = version
        self.id = id
        self.params = {
            'access_token' : self.token,
            'v' : self.version
        }

    def username(self):
        params_user = self.params.copy()
        params_user['user_ids'] = self.id
        resp = requests.get(self.url + 'users.get', params_user)
        return resp.json()['response'][0]['first_name'] + ' ' + resp.json()['response'][0]['last_name']
    
    def friends(self):
        params_friends = self.params.copy()
        params_friends['user_id'] = self.id
        resp = requests.get(self.url + 'friends.get', params_friends)
        return resp.json()['response']['items']

    def __and__(self,other):
        friends1 = set(self.friends())
        friends2 = set(other.friends())
        return list(friends1 & friends2)
    
    def __str__(self):
        return (f'https://vk.com/id{self.id}')
        

token = ''
user1 = VkUser(token,5.131,16329774)
user2 = VkUser(token,5.131,24657874)
for friend in (user1 & user2):
     user = VkUser(token,5.131,friend)
     print(user)

