"""
get https request content from feedernet using mitmproxy

@reference mitmproxy, https://mitmproxy.org/
@author Chanwoo Gwon, Yonsei Univ. Researcher, since 2020.05.~
@Date 2021.03.18
"""
from mitmproxy import ctx


class Counter:
    def __init__(self):
        self.num = 0

    def request(self, flow):
        self.num = self.num + 1
        ctx.log.info("We've seen %d flows" % self.num)


addons = [
    Counter()
]