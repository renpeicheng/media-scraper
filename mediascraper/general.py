#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 Elvis Yu-Jing Lin <elvisyjlin@gmail.com>
# Licensed under the MIT License - https://opensource.org/licenses/MIT

import mediascrapers
import sys

if __name__ == '__main__':
    scraper = mediascrapers.MediaScraper(mode='normal', debug=False)
    scraper.connect(sys.argv[1])
    scraper.scrape(path='download/general')