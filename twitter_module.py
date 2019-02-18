from TwitterAPI import TwitterAPI
import json

consumer_key = 'UEfv601MdQ6bUP9KuwdLLVrrx'
consumer_secret = 'Rah9B8iUhY8kJy9DnjS3QpGkVVR2abTGWnajVpXffx8LEJ2f4t'
access_token_key = '2954340437-BwU0vxDvG9NZmfccnC4kWJC1so784HQlfFjcz33'
access_token_secret = 'T0gBAxByfxRAj9x1RPHAiovWF3gxTEfv82JscbQ8KsibT'


def tw_read():
    # If you are behind a firewall you may need to provide proxy server
    # authentication.
    proxy_url = None  # Example: 'https://USERNAME:PASSWORD@PROXYSERVER:PORT'

    # Using OAuth 1.0 to authenticate you have access all Twitter endpoints.
    api = TwitterAPI(consumer_key,
                     consumer_secret,
                     access_token_key,
                     access_token_secret,
                     auth_type='oAuth1',
                     proxy_url=proxy_url)
    # r = api.request('application/rate_limit_status')
    r = api.request('friends/list', {'include_user_entities': False})
    print('This module is made to find important information from user list of @inspired_ann.')
    choose_1 = input('Please, choose the way to work with json.\n'
                     '1 - to read information for whole users\n'
                     '2 - to read information for specified user\n'
                     ':')

    print('Print one type of information from the bottom list you would like to find:\n'
          '> id\n'
          '> name\n'
          '> location\n'
          '> url\n'
          '> description\n'
          '> followers_count\n'
          '> friends_count\n'
          '> status\n')
    first_req = input(':')
    # Parse the JSON response.
    j = r.response.json()
    try:
        if first_req != '':
            if choose_1 == '1':
                ret_dict = dict()
                for i in range(len(j['users'])):
                    first_req_res = j['users'][i][first_req]
                    if first_req_res == '':
                        first_req_res = None
                    ret_dict[j['users'][i]['screen_name']] = first_req_res
                    print('{} : {}'.format(j['users'][i]['screen_name'], first_req_res))


            if choose_1 == '2':
                SCREEN_NAME = input('Enter the nickname(screen name) of user (e.g. usuprun): ')
                ret_dict = dict()
                for i in range(len(j['users'])):
                    if j['users'][i]['screen_name'] == SCREEN_NAME:
                        first_req_res = j['users'][i][first_req]
                        if first_req_res == '':
                            first_req_res = None
                        print('{} : {}'.format(j['users'][i]['screen_name'], first_req_res))
                        ret_dict[SCREEN_NAME] = first_req_res

            with open('data.json', 'w') as outfile:
                json.dump(j, outfile)



        else:
            finish = input('Hmm, you entered something else.\n'
                           'Print "exit" if you want to finish\n'
                           'Or print "again" to restart\n'
                           ':')
            if finish == 'again':
                tw_read()
            else:
                return None

    except UnboundLocalError:
        finish = ('There is no variable {} in this dictionary\n'.format(first_req),
              'Enter "again" to restart\n'
              'Or print "exit" if you want to finish\n'
              ':')
        if finish == 'again':
            tw_read()
        else:
            return None
    print('Now check your folder, there is a new file "data.json" with the whole json from Twitter API.\n'
          'This program returns dict from your request.')
    return ret_dict

tw_read()