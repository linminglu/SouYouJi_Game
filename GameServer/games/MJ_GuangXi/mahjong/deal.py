# -*- coding:utf-8 -*-
# !/usr/bin/python
"""
Author:$Author$
Date:$Date$
Revision:$Revision$

Description:
    发牌管理器
"""
from common.deal_manage import DealMgr
from common.card_define import *


class DealManager(DealMgr):
    """
    发牌管理器
    """

    def getDealSetting(self):
        """
        设置发牌器参数
        """
        self.setting = {
            'MAX_TILES_NUM': 9,
            'MAX_REPEAT_COUNT': 4,
            'HAND_TILES_COUNT': 13,
            'INVALID_TILES_COUNT': self.game.catchHourseCount_SelfHu,
            # 常规牌
            'NORMAL_TILES': [CHARACTER, DOT, BAMBOO],
            # 字牌[中发白,东南西北]
            'HONOR_TILES': [RED, WHITE, GREEN, EAST, WEST, SOUTH, NORTH],
            # 花牌
            'FLOWER_TILES': []
        }
