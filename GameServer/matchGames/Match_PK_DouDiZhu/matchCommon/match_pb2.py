# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: match.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='match.proto',
  package='match',
  serialized_pb='\n\x0bmatch.proto\x12\x05match\"\x15\n\x13\x43_S_Need_To_Refresh\"*\n\x13S_C_Need_To_Refresh\x12\x13\n\x0brefreshType\x18\x01 \x02(\x07\"C\n\rS_C_NoticeMsg\x12\x10\n\x08msg_type\x18\x01 \x02(\x07\x12\x13\n\x0b\x61\x63tion_type\x18\x02 \x01(\x07\x12\x0b\n\x03msg\x18\x03 \x02(\t\"\x0f\n\rC_S_MatchInfo\"\xd2\x01\n\rS_C_MatchInfo\x12\x13\n\x0bmatchNumber\x18\x01 \x02(\t\x12\x12\n\ngameNumber\x18\x02 \x01(\t\x12\x10\n\x08\x64\x65scribe\x18\x03 \x01(\t\x12\x13\n\x0b\x63urRoundNum\x18\x04 \x01(\x07\x12\x13\n\x0bmaxRoundNum\x18\x05 \x01(\x07\x12\x14\n\x0c\x63urPlayerNum\x18\x06 \x01(\x07\x12\x14\n\x0cmaxPlayerNum\x18\x07 \x01(\x07\x12\x13\n\x0b\x63urRotation\x18\x08 \x01(\x07\x12\x1b\n\x13\x63urRotationRoundNum\x18\t \x01(\x07\"\x13\n\x11\x43_S_RotationDatas\"\xc7\x01\n\x11S_C_RotationDatas\x12<\n\rRotationDatas\x18\x01 \x03(\x0b\x32%.match.S_C_RotationDatas.RotationData\x1at\n\x0cRotationData\x12\x10\n\x08rotation\x18\x01 \x01(\x07\x12\x0c\n\x04type\x18\x02 \x01(\x07\x12\x16\n\x0etotalPlayerNum\x18\x03 \x01(\x07\x12\x17\n\x0ftargetPlayerNum\x18\x04 \x01(\x07\x12\x13\n\x0btargetRound\x18\x05 \x01(\x07\"Z\n\x15S_C_curRoundRoomDatas\x12\x12\n\ntotalCount\x18\x01 \x01(\x07\x12\x17\n\x0fnotBalanceCount\x18\x02 \x01(\x07\x12\x14\n\x0c\x62\x61lanceCount\x18\x03 \x01(\x07\"\xb3\x01\n\x10S_C_RoundBalance\x12\x13\n\x0b\x62\x61lanceType\x18\x01 \x01(\x07\x12\x13\n\x0b\x62\x61lanceRank\x18\x02 \x01(\x07\x12!\n\x08rewardId\x18\x03 \x01(\x0e\x32\x0f.match.Currency\x12\x11\n\trewardNum\x18\x04 \x01(\x07\"?\n\x10\x65num_balanceType\x12\x08\n\x04wait\x10\x01\x12\x08\n\x04rise\x10\x02\x12\r\n\teliminate\x10\x03\x12\x08\n\x04rank\x10\x04\";\n\x0c\x43_S_RankInfo\x12\x14\n\x0cgetRoomRanks\x18\x01 \x01(\x08\x12\x15\n\rgetMatchRanks\x18\x02 \x01(\x08\"\x80\x02\n\x0cS_C_RankInfo\x12\x30\n\troomRanks\x18\x01 \x03(\x0b\x32\x1d.match.S_C_RankInfo.rank_info\x12\x31\n\nmatchRanks\x18\x02 \x03(\x0b\x32\x1d.match.S_C_RankInfo.rank_info\x1a\x8a\x01\n\trank_info\x12\x0c\n\x04side\x18\x01 \x02(\x0f\x12\x0b\n\x03uid\x18\x02 \x02(\x07\x12\x10\n\x08nickname\x18\x03 \x02(\t\x12\x12\n\nheadImgUrl\x18\x04 \x02(\t\x12\x0c\n\x04rank\x18\x05 \x02(\x07\x12\x15\n\rintegralTotal\x18\x06 \x02(\x0f\x12\x17\n\x0fintegralHistory\x18\x07 \x03(\x0f\"\x13\n\x11\x43_S_getRewardList\"\'\n\x11S_C_getRewardList\x12\x12\n\nrewardList\x18\x0b \x01(\t*\xc2\x02\n\nMSG_HEADER\x12\x19\n\x13\x43_S_NEED_TO_REFRESH\x10\x81\x80\x03\x12\x13\n\rC_S_MATCHINFO\x10\x83\x80\x03\x12\x12\n\x0c\x43_S_RANKINFO\x10\x84\x80\x03\x12\x17\n\x11\x43_S_ROTATIONDATAS\x10\x85\x80\x03\x12\x17\n\x11\x43_S_GETREWARDLIST\x10\x88\x80\x03\x12\x19\n\x13S_C_NEED_TO_REFRESH\x10\x81\xa0\x03\x12\x13\n\rS_C_NOTICEMSG\x10\x82\xa0\x03\x12\x13\n\rS_C_MATCHINFO\x10\x83\xa0\x03\x12\x12\n\x0cS_C_RANKINFO\x10\x84\xa0\x03\x12\x17\n\x11S_C_ROTATIONDATAS\x10\x85\xa0\x03\x12\x1b\n\x15S_C_CURROUNDROOMDATAS\x10\x86\xa0\x03\x12\x16\n\x10S_C_ROUNDBALANCE\x10\x87\xa0\x03\x12\x17\n\x11S_C_GETREWARDLIST\x10\x88\xa0\x03*>\n\x08\x43urrency\x12\x08\n\x04none\x10\x00\x12\x0c\n\x08roomCard\x10\x01\x12\x0b\n\x07yyPoint\x10\x02\x12\r\n\tgamePoint\x10\x03')

_MSG_HEADER = _descriptor.EnumDescriptor(
  name='MSG_HEADER',
  full_name='match.MSG_HEADER',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='C_S_NEED_TO_REFRESH', index=0, number=49153,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C_S_MATCHINFO', index=1, number=49155,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C_S_RANKINFO', index=2, number=49156,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C_S_ROTATIONDATAS', index=3, number=49157,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C_S_GETREWARDLIST', index=4, number=49160,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S_C_NEED_TO_REFRESH', index=5, number=53249,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S_C_NOTICEMSG', index=6, number=53250,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S_C_MATCHINFO', index=7, number=53251,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S_C_RANKINFO', index=8, number=53252,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S_C_ROTATIONDATAS', index=9, number=53253,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S_C_CURROUNDROOMDATAS', index=10, number=53254,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S_C_ROUNDBALANCE', index=11, number=53255,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S_C_GETREWARDLIST', index=12, number=53256,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1268,
  serialized_end=1590,
)

MSG_HEADER = enum_type_wrapper.EnumTypeWrapper(_MSG_HEADER)
_CURRENCY = _descriptor.EnumDescriptor(
  name='Currency',
  full_name='match.Currency',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='none', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='roomCard', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='yyPoint', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='gamePoint', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1592,
  serialized_end=1654,
)

Currency = enum_type_wrapper.EnumTypeWrapper(_CURRENCY)
C_S_NEED_TO_REFRESH = 49153
C_S_MATCHINFO = 49155
C_S_RANKINFO = 49156
C_S_ROTATIONDATAS = 49157
C_S_GETREWARDLIST = 49160
S_C_NEED_TO_REFRESH = 53249
S_C_NOTICEMSG = 53250
S_C_MATCHINFO = 53251
S_C_RANKINFO = 53252
S_C_ROTATIONDATAS = 53253
S_C_CURROUNDROOMDATAS = 53254
S_C_ROUNDBALANCE = 53255
S_C_GETREWARDLIST = 53256
none = 0
roomCard = 1
yyPoint = 2
gamePoint = 3


_S_C_ROUNDBALANCE_ENUM_BALANCETYPE = _descriptor.EnumDescriptor(
  name='enum_balanceType',
  full_name='match.S_C_RoundBalance.enum_balanceType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='wait', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='rise', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='eliminate', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='rank', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=820,
  serialized_end=883,
)


_C_S_NEED_TO_REFRESH = _descriptor.Descriptor(
  name='C_S_Need_To_Refresh',
  full_name='match.C_S_Need_To_Refresh',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=22,
  serialized_end=43,
)


_S_C_NEED_TO_REFRESH = _descriptor.Descriptor(
  name='S_C_Need_To_Refresh',
  full_name='match.S_C_Need_To_Refresh',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='refreshType', full_name='match.S_C_Need_To_Refresh.refreshType', index=0,
      number=1, type=7, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=45,
  serialized_end=87,
)


_S_C_NOTICEMSG = _descriptor.Descriptor(
  name='S_C_NoticeMsg',
  full_name='match.S_C_NoticeMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg_type', full_name='match.S_C_NoticeMsg.msg_type', index=0,
      number=1, type=7, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='action_type', full_name='match.S_C_NoticeMsg.action_type', index=1,
      number=2, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msg', full_name='match.S_C_NoticeMsg.msg', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=89,
  serialized_end=156,
)


_C_S_MATCHINFO = _descriptor.Descriptor(
  name='C_S_MatchInfo',
  full_name='match.C_S_MatchInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=158,
  serialized_end=173,
)


_S_C_MATCHINFO = _descriptor.Descriptor(
  name='S_C_MatchInfo',
  full_name='match.S_C_MatchInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='matchNumber', full_name='match.S_C_MatchInfo.matchNumber', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gameNumber', full_name='match.S_C_MatchInfo.gameNumber', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='describe', full_name='match.S_C_MatchInfo.describe', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='curRoundNum', full_name='match.S_C_MatchInfo.curRoundNum', index=3,
      number=4, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='maxRoundNum', full_name='match.S_C_MatchInfo.maxRoundNum', index=4,
      number=5, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='curPlayerNum', full_name='match.S_C_MatchInfo.curPlayerNum', index=5,
      number=6, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='maxPlayerNum', full_name='match.S_C_MatchInfo.maxPlayerNum', index=6,
      number=7, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='curRotation', full_name='match.S_C_MatchInfo.curRotation', index=7,
      number=8, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='curRotationRoundNum', full_name='match.S_C_MatchInfo.curRotationRoundNum', index=8,
      number=9, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=176,
  serialized_end=386,
)


_C_S_ROTATIONDATAS = _descriptor.Descriptor(
  name='C_S_RotationDatas',
  full_name='match.C_S_RotationDatas',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=388,
  serialized_end=407,
)


_S_C_ROTATIONDATAS_ROTATIONDATA = _descriptor.Descriptor(
  name='RotationData',
  full_name='match.S_C_RotationDatas.RotationData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rotation', full_name='match.S_C_RotationDatas.RotationData.rotation', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='match.S_C_RotationDatas.RotationData.type', index=1,
      number=2, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='totalPlayerNum', full_name='match.S_C_RotationDatas.RotationData.totalPlayerNum', index=2,
      number=3, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='targetPlayerNum', full_name='match.S_C_RotationDatas.RotationData.targetPlayerNum', index=3,
      number=4, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='targetRound', full_name='match.S_C_RotationDatas.RotationData.targetRound', index=4,
      number=5, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=493,
  serialized_end=609,
)

_S_C_ROTATIONDATAS = _descriptor.Descriptor(
  name='S_C_RotationDatas',
  full_name='match.S_C_RotationDatas',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='RotationDatas', full_name='match.S_C_RotationDatas.RotationDatas', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_S_C_ROTATIONDATAS_ROTATIONDATA, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=410,
  serialized_end=609,
)


_S_C_CURROUNDROOMDATAS = _descriptor.Descriptor(
  name='S_C_curRoundRoomDatas',
  full_name='match.S_C_curRoundRoomDatas',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='totalCount', full_name='match.S_C_curRoundRoomDatas.totalCount', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='notBalanceCount', full_name='match.S_C_curRoundRoomDatas.notBalanceCount', index=1,
      number=2, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='balanceCount', full_name='match.S_C_curRoundRoomDatas.balanceCount', index=2,
      number=3, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=611,
  serialized_end=701,
)


_S_C_ROUNDBALANCE = _descriptor.Descriptor(
  name='S_C_RoundBalance',
  full_name='match.S_C_RoundBalance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='balanceType', full_name='match.S_C_RoundBalance.balanceType', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='balanceRank', full_name='match.S_C_RoundBalance.balanceRank', index=1,
      number=2, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rewardId', full_name='match.S_C_RoundBalance.rewardId', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rewardNum', full_name='match.S_C_RoundBalance.rewardNum', index=3,
      number=4, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _S_C_ROUNDBALANCE_ENUM_BALANCETYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=704,
  serialized_end=883,
)


_C_S_RANKINFO = _descriptor.Descriptor(
  name='C_S_RankInfo',
  full_name='match.C_S_RankInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='getRoomRanks', full_name='match.C_S_RankInfo.getRoomRanks', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='getMatchRanks', full_name='match.C_S_RankInfo.getMatchRanks', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=885,
  serialized_end=944,
)


_S_C_RANKINFO_RANK_INFO = _descriptor.Descriptor(
  name='rank_info',
  full_name='match.S_C_RankInfo.rank_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='side', full_name='match.S_C_RankInfo.rank_info.side', index=0,
      number=1, type=15, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uid', full_name='match.S_C_RankInfo.rank_info.uid', index=1,
      number=2, type=7, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nickname', full_name='match.S_C_RankInfo.rank_info.nickname', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='headImgUrl', full_name='match.S_C_RankInfo.rank_info.headImgUrl', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rank', full_name='match.S_C_RankInfo.rank_info.rank', index=4,
      number=5, type=7, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='integralTotal', full_name='match.S_C_RankInfo.rank_info.integralTotal', index=5,
      number=6, type=15, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='integralHistory', full_name='match.S_C_RankInfo.rank_info.integralHistory', index=6,
      number=7, type=15, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1065,
  serialized_end=1203,
)

_S_C_RANKINFO = _descriptor.Descriptor(
  name='S_C_RankInfo',
  full_name='match.S_C_RankInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='roomRanks', full_name='match.S_C_RankInfo.roomRanks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='matchRanks', full_name='match.S_C_RankInfo.matchRanks', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_S_C_RANKINFO_RANK_INFO, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=947,
  serialized_end=1203,
)


_C_S_GETREWARDLIST = _descriptor.Descriptor(
  name='C_S_getRewardList',
  full_name='match.C_S_getRewardList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1205,
  serialized_end=1224,
)


_S_C_GETREWARDLIST = _descriptor.Descriptor(
  name='S_C_getRewardList',
  full_name='match.S_C_getRewardList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rewardList', full_name='match.S_C_getRewardList.rewardList', index=0,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1226,
  serialized_end=1265,
)

_S_C_ROTATIONDATAS_ROTATIONDATA.containing_type = _S_C_ROTATIONDATAS;
_S_C_ROTATIONDATAS.fields_by_name['RotationDatas'].message_type = _S_C_ROTATIONDATAS_ROTATIONDATA
_S_C_ROUNDBALANCE.fields_by_name['rewardId'].enum_type = _CURRENCY
_S_C_ROUNDBALANCE_ENUM_BALANCETYPE.containing_type = _S_C_ROUNDBALANCE;
_S_C_RANKINFO_RANK_INFO.containing_type = _S_C_RANKINFO;
_S_C_RANKINFO.fields_by_name['roomRanks'].message_type = _S_C_RANKINFO_RANK_INFO
_S_C_RANKINFO.fields_by_name['matchRanks'].message_type = _S_C_RANKINFO_RANK_INFO
DESCRIPTOR.message_types_by_name['C_S_Need_To_Refresh'] = _C_S_NEED_TO_REFRESH
DESCRIPTOR.message_types_by_name['S_C_Need_To_Refresh'] = _S_C_NEED_TO_REFRESH
DESCRIPTOR.message_types_by_name['S_C_NoticeMsg'] = _S_C_NOTICEMSG
DESCRIPTOR.message_types_by_name['C_S_MatchInfo'] = _C_S_MATCHINFO
DESCRIPTOR.message_types_by_name['S_C_MatchInfo'] = _S_C_MATCHINFO
DESCRIPTOR.message_types_by_name['C_S_RotationDatas'] = _C_S_ROTATIONDATAS
DESCRIPTOR.message_types_by_name['S_C_RotationDatas'] = _S_C_ROTATIONDATAS
DESCRIPTOR.message_types_by_name['S_C_curRoundRoomDatas'] = _S_C_CURROUNDROOMDATAS
DESCRIPTOR.message_types_by_name['S_C_RoundBalance'] = _S_C_ROUNDBALANCE
DESCRIPTOR.message_types_by_name['C_S_RankInfo'] = _C_S_RANKINFO
DESCRIPTOR.message_types_by_name['S_C_RankInfo'] = _S_C_RANKINFO
DESCRIPTOR.message_types_by_name['C_S_getRewardList'] = _C_S_GETREWARDLIST
DESCRIPTOR.message_types_by_name['S_C_getRewardList'] = _S_C_GETREWARDLIST

class C_S_Need_To_Refresh(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C_S_NEED_TO_REFRESH

  # @@protoc_insertion_point(class_scope:match.C_S_Need_To_Refresh)

class S_C_Need_To_Refresh(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S_C_NEED_TO_REFRESH

  # @@protoc_insertion_point(class_scope:match.S_C_Need_To_Refresh)

class S_C_NoticeMsg(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S_C_NOTICEMSG

  # @@protoc_insertion_point(class_scope:match.S_C_NoticeMsg)

class C_S_MatchInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C_S_MATCHINFO

  # @@protoc_insertion_point(class_scope:match.C_S_MatchInfo)

class S_C_MatchInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S_C_MATCHINFO

  # @@protoc_insertion_point(class_scope:match.S_C_MatchInfo)

class C_S_RotationDatas(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C_S_ROTATIONDATAS

  # @@protoc_insertion_point(class_scope:match.C_S_RotationDatas)

class S_C_RotationDatas(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class RotationData(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _S_C_ROTATIONDATAS_ROTATIONDATA

    # @@protoc_insertion_point(class_scope:match.S_C_RotationDatas.RotationData)
  DESCRIPTOR = _S_C_ROTATIONDATAS

  # @@protoc_insertion_point(class_scope:match.S_C_RotationDatas)

class S_C_curRoundRoomDatas(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S_C_CURROUNDROOMDATAS

  # @@protoc_insertion_point(class_scope:match.S_C_curRoundRoomDatas)

class S_C_RoundBalance(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S_C_ROUNDBALANCE

  # @@protoc_insertion_point(class_scope:match.S_C_RoundBalance)

class C_S_RankInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C_S_RANKINFO

  # @@protoc_insertion_point(class_scope:match.C_S_RankInfo)

class S_C_RankInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class rank_info(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _S_C_RANKINFO_RANK_INFO

    # @@protoc_insertion_point(class_scope:match.S_C_RankInfo.rank_info)
  DESCRIPTOR = _S_C_RANKINFO

  # @@protoc_insertion_point(class_scope:match.S_C_RankInfo)

class C_S_getRewardList(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C_S_GETREWARDLIST

  # @@protoc_insertion_point(class_scope:match.C_S_getRewardList)

class S_C_getRewardList(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S_C_GETREWARDLIST

  # @@protoc_insertion_point(class_scope:match.S_C_getRewardList)


# @@protoc_insertion_point(module_scope)
