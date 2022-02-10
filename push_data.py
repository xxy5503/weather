# -*- coding:utf-8 -*-
import requests


class PushData:
    def push_data(self, location_dict, daily_dict):
        #向微信推送天气消息
        self.url = 'https://www.pushplus.plus/send?'
        self.payload = {'token': '', 'title': '', 'content ': '', 'template ': 'markdown', 'topic': 'op'}
        # 消息推送Key
        self.token = '00274b7c5fa242ed8b6fa9f193c21656'
        self.payload['token'] = self.token
        # 推送消息Title
        self.title = '%s 天气预报' % location_dict['name']
        self.payload['title'] = self.title
        # 推送消息Description
        self.content = '<b># 今日天气</b>\n* 日间最高温度：%s℃，%s\n* 夜间最高温度：%s℃，%s\n* 相对湿度：%s %%  \n* 风向：%s\n* 风力：%s 级\n* 风速：%s KM/H\n\n<b># 明日天气</b>\n* 日间最高温度：%s℃，%s\n* 夜间最高温度：%s℃，%s\n* 相对湿度：%s %% \n* 风向：%s\n* 风力：%s 级\n* 风速：%s KM/H' % (
            daily_dict[0]['high'], daily_dict[0]['text_day'], daily_dict[0]['low'], daily_dict[0]['text_night'], daily_dict[0]['humidity'], daily_dict[0]['wind_direction'], daily_dict[0]['wind_scale'], daily_dict[0]['wind_speed'], daily_dict[1]['high'], daily_dict[1]['text_day'], daily_dict[1]['low'], daily_dict[1]['text_night'], daily_dict[1]['humidity'], daily_dict[1]['wind_direction'], daily_dict[1]['wind_scale'], daily_dict[1]['wind_speed'])
        self.payload['content'] = self.content
        requests.get(self.url, params=self.payload)