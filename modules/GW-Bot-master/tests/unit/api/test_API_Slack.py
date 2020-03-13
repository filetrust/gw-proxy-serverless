import sys
import unittest

from pbx_gs_python_utils.utils.Dev import Dev

from gw_bot.api.API_Slack import API_Slack
from gw_bot.helpers.Lambda_Helpers import screenshot_from_url
from gw_bot.helpers.Test_Helper import Test_Helper


class test_API_Slack(Test_Helper):

    def setUp(self):
        super().setUp()
        self.channel = 'CSK9RADE2' #''gs-bot-tests'
        self.api     = API_Slack(self.channel)
        self.result  = None

    def tearDown(self):
        if self.result is not None:
            Dev.pprint(self.result)

    def test_add_reaction(self):
        response = self.api.send_message("Testing reaction")
        ts       = response['message']['ts']
        response = self.api.add_reaction(ts, "thumbsup")
        self.api.add_reaction(ts, "point_down")
        assert response['ok'] is True

    # def test_channels_public(self):
    #     channels = self.api.channels_public()
    #     self.result = channels
    #     #assert len(set(channels)) > 40
    #     #assert channels['random']['id'] == 'C7EUMACGJ'
    #
    # def test_channels_private(self):
    #     channels = self.api.channels_private()
    #     assert 'gs-bot-tests' in list(set(channels))

    # def test_delete_message(self):
    #     reply_send   = self.api.send_message('to delete 123')      # send message
    #     ts           = reply_send['message']['ts']                 # get timestamp of message posted
    #     reply_delete = self.api.delete_message(ts)                 # delete message
    #     assert reply_delete['ok'] is True
    #     assert reply_delete['ts'] == ts
    #

    def test_files_info(self):
        file_id = 'FSJNZ8V5F'
        self.result = self.api.files_info(file_id)

    # def test_get_channel(self):
    #     response = self.api.get_channel('DDKUZTK6X')
    #     assert response.get('error') == 'method_not_supported_for_channel_type'
    #
    # def test_get_messages(self):
    #     assert len(self.api.get_messages('DDKUZTK6X')) == 10

    def test_send_message(self):
        text    = 'testing api_slack 123'
        result = self.api.send_message(text)

        assert result['ok'] is True
        # del result['message']['ts']
        # assert result['message'] == {   'bot_id'  : 'BDKLUMX4K'            ,
        #                                 'subtype' : 'bot_message'          ,
        #                                 'text'    : 'testing api_slack 123',
        #                                 'type'    : 'message'              ,
        #                                 'username': 'gs-bot'               }

    def test_user(self):
        user_id = 'UDK5W7W3T'
        result = self.api.send_message(user_id)
        assert result['message']['username'] == 'GW-Bot'

    # def test_users(self):
    #     users = self.api.users()
    #     assert len(set(users)) > 120
    #     assert users['dinis.cruz']['id'] == 'U7ESE1XS7'
    #     assert users['gsbot'     ]['id'] == 'UDK5W7W3T'


    # @unittest.skip('sends message do gsbot user and not a dedicated channel')
    # def test_send_and_receive_messages(self):
    #     message_ts = self.api.send_message('<@UDK5W7W3T> hello', channel='DDKUZTK6X').get('message').get('ts')
    #     #Misc.wait(0.1)
    #     messages = self.api.get_messages(channel='DDKUZTK6X',limit=2)
    #     assert messages == ['<@UDK5W7W3T> hello', '<@UDK5W7W3T> hello']
    #     self.api.delete_message(message_ts)                                 # doesn't seem to be working


    ## Buttons and interaction

    def test____message_with_button(self):
        message = {
                "text": "Would you like to play a game?",
                "attachments": [
                    {
                        "aaaaa" : "bbbbb",
                        "ccccc" : "ddddd",
                        "text": "Choose a game to play",
                        "fallback": "You are unable to choose a game",
                        "callback_id": "wopr_game",
                        "color": "#3AA3E3",
                        "attachment_type": "default",
                        "actions": [
                            {
                                "name": "game",
                                "text": "Chess",
                                "type": "button",
                                "value": "chess"
                            },
                            {
                                "name": "game",
                                "text": "Falken's Maze",
                                "type": "button",
                                "value": "maze"
                            },
                            {
                                "name": "THE NAME ",
                                "text": "BETTER OPTION",
                                "type": "button",
                                "value": "THE VALUE"
                            },
                            {
                                "name": "game",
                                "text": "Thermonuclear War",
                                "style": "danger",
                                "type": "button",
                                "value": "war",
                                "confirm": {
                                    "title": "Are you sure?",
                                    "text": "Wouldn't you prefer a good game of chess?",
                                    "ok_text": "Yes",
                                    "dismiss_text": "No"
                                }
                            },
                            {
                                    "name": "games_list",
                                    "text": "Pick a game...",
                                    "type": "select",
                                    "options": [
                                        {
                                            "text": "Hearts",
                                            "value": "hearts"
                                        },
                                        {
                                            "text": "Bridge",
                                            "value": "bridge"
                                        },
                                        {
                                            "text": "Checkers",
                                            "value": "checkers"
                                        },
                                        {
                                            "text": "Chess",
                                            "value": "chess"
                                        },
                                        {
                                            "text": "Poker",
                                            "value": "poker"
                                        },
                                        {
                                            "text": "Falken's Maze",
                                            "value": "maze"
                                        },
                                        {
                                            "text": "test 1",
                                            "value": "test 1"
                                        }
                                        ,
                                        {
                                            "text": "test 2",
                                            "value": "test 2"
                                        }
                                        ,
                                        {
                                            "text": "test 3",
                                            "value": "test 3"
                                        }
                                        ,
                                        {
                                            "text": "test 4",
                                            "value": "test 4"
                                        }
                                        ,
                                        {
                                            "text": "test 4",
                                            "value": "test 4"
                                        }
                                        ,
                                        {
                                            "text": "test 5",
                                            "value": "test 5"
                                        }
                                    ]
                                }

                        ]
                    }
                ]
            }
        self.api.send_message(message['text'], message['attachments'])

    ## methods using lambdas

    # def test_dot_to_slack(self):
    #     dot = 'digraph {\n a->b \n}'
    #     assert self.api.dot_to_slack(dot) == 'image sent .... '
    #
    # def test_puml_to_slack(self):
    #     puml = "@startuml \n aaa->bbb \n @enduml"
    #     assert self.api.puml_to_slack(puml) == 'image sent .... '

    def test_upload_file(self):
        target_file = '/tmp/test_file.png'
        channel     = 'CSK9RADE2' #'DRE51D4EM'
        title       = 'file upload'
        self.api.upload_file(target_file,channel, title)

    def test_upload_image_from_png_base64(self):
        title    = 'Google'
        channel  = 'DRE51D4EM' #'CSK9RADE2'  #
        url      = 'https://www.google.com'
        png_data = screenshot_from_url(url)
        self.result = self.api.upload_image_from_png_base64(png_data, channel, title)

