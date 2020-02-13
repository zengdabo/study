#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# "a test to spider a html page and print the meeting msg to txt."
from urllib import request
from html.parser import HTMLParser
from html.entities import name2codepoint


class myhtmlparser(HTMLParser):
    _tag_name = ""
    _attrs_name = ("",)
    _data_name = ""

    def handle_starttag(self, tag, attrs):
        if len(attrs) >= 1:
            if (
                attrs[0][0] == "class"
                and (
                    attrs[0][1] == "event-title"
                    or attrs[0][1] == "widget-title"
                    or attrs[0][1] == "event-location"
                )
            ) or attrs[0][0] == "datetime":
                self._tag_name = tag
                self._attrs_name = attrs
                print("...")

    def handle_data(self, data):
        if self._tag_name != "":
            print(data)

    def handle_endtag(self, tag):
        if tag == self._tag_name:
            self._tag_name = ""
            self._attrs_name = ("",)


def url2html(url):
    with request.urlopen(url) as f:
        html_get = f.read().decode(encoding="utf_8")
    return html_get


url_name = "https://www.python.org/events/python-events/"
meetingpars = myhtmlparser()
htmlcontent = url2html(url_name)
meetingpars.feed(htmlcontent)
