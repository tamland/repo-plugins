# -*- coding: utf-8 -*-
# Copyright: (c) 2017, SylvainCecchetto
# GNU General Public License v2.0+ (see LICENSE.txt or https://www.gnu.org/licenses/gpl-2.0.txt)

# This file is part of Catch-up TV & More

from __future__ import unicode_literals
import re
import urlquick

# noinspection PyUnresolvedReferences
from codequick import Resolver

from resources.lib import resolver_proxy, web_utils

URL_LIVE = 'https://www.m24tv.ma/'
DIRECT_URL_LIVE = 'https://63df3191463ce.streamlock.net/live/ngrp:Live2.stream_all/playlist.m3u8'

GENERIC_HEADERS = {'User-Agent': web_utils.get_random_windows_ua()}


@Resolver.register
def get_live_url(plugin, item_id, **kwargs):

    try:
        resp = urlquick.get(URL_LIVE, headers=GENERIC_HEADERS, max_age=-1)
        video_url = re.compile(r'\"file\"\:\ \"(.*\.m3u8.*)\"\,').findall(resp.text)[0]

    except Exception:
        video_url = DIRECT_URL_LIVE

    return resolver_proxy.get_stream_with_quality(plugin, video_url)
