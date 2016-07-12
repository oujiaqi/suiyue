#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import tornado.web

from article import ArticleHandler
from card import CardHandler, WcardHandler
from fans import FansHandler
from free import FreeHandler
from index import IndexHandler
from login import LoginHandler
from logout import LogoutHandler
from read import ReadHandler
from setting import ChangeHandler
from signin import SigninHandler
from story import StoryHandler, WstoryHandler
from user import UserHandler, FocusHandler
from write import WriteHandler

application = tornado.web.Application(
        handlers=[(r'/login', LoginHandler),(r'/',IndexHandler),(r'/read',ReadHandler),(r'/signin',SigninHandler),(r'/logout',LogoutHandler),(r'/article',ArticleHandler),(r'/story',StoryHandler),(r'/card',CardHandler),(r'/user',UserHandler),(r'/free',FreeHandler),(r'/write',WriteHandler),(r'/focus',FocusHandler),(r'/change',ChangeHandler),(r'/wcard',WcardHandler),(r'/wstory',WstoryHandler),(r"/fans",FansHandler)],
        template_path=os.path.join(os.path.dirname(__file__), "../views"),
        static_path=os.path.join(os.path.dirname(__file__), "../public"),
        debug=True,
        cookie_secret="61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo="
        )