"""
get https request content from feedernet using mitmproxy

@reference mitmproxy, https://mitmproxy.org/
@author Chanwoo Gwon, Yonsei Univ. Researcher, since 2020.05.~
@Date 2021.03.18
"""
from mitmproxy import ctx
from lib.database import DataManager
from config import Config


class PacketManager:
    def __init__(self):
        self.database = DataManager(
            Config.DATABASE_HOST,
            Config.DATABASE,
            Config.DATABASE_USER,
            Config.DATABASE_PASSWORD
        )

    def response(self, flow):
        self.database.insert_data(
            flow.request.method,
            "{0}".format(flow.client_conn.address[0]),
            flow.request.content.decode("utf-8"),
            "{0}:{1}{2}".format(flow.server_conn.address[0], flow.server_conn.address[1], flow.request.path),
            flow.response.content.decode("utf-8"))



addons = [
    PacketManager()
]
