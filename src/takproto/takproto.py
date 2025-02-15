# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: proto/tak.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class Contact(betterproto.Message):
    endpoint: str = betterproto.string_field(1)
    callsign: str = betterproto.string_field(2)


@dataclass
class Status(betterproto.Message):
    battery: int = betterproto.uint32_field(1)


@dataclass
class Group(betterproto.Message):
    name: str = betterproto.string_field(1)
    role: str = betterproto.string_field(2)


@dataclass
class PrecisionLocation(betterproto.Message):
    geopointsrc: str = betterproto.string_field(1)
    altsrc: str = betterproto.string_field(2)


@dataclass
class Takv(betterproto.Message):
    device: str = betterproto.string_field(1)
    platform: str = betterproto.string_field(2)
    os: str = betterproto.string_field(3)
    version: str = betterproto.string_field(4)


@dataclass
class Track(betterproto.Message):
    speed: float = betterproto.double_field(1)
    course: float = betterproto.double_field(2)


@dataclass
class Detail(betterproto.Message):
    xml_detail: str = betterproto.string_field(1)
    contact: "Contact" = betterproto.message_field(2)
    group: "Group" = betterproto.message_field(3)
    precision_location: "PrecisionLocation" = betterproto.message_field(4)
    status: "Status" = betterproto.message_field(5)
    takv: "Takv" = betterproto.message_field(6)
    track: "Track" = betterproto.message_field(7)


@dataclass
class CotEvent(betterproto.Message):
    type: str = betterproto.string_field(1)
    access: str = betterproto.string_field(2)
    qos: str = betterproto.string_field(3)
    opex: str = betterproto.string_field(4)
    uid: str = betterproto.string_field(5)
    send_time: int = betterproto.uint64_field(6)
    start_time: int = betterproto.uint64_field(7)
    stale_time: int = betterproto.uint64_field(8)
    how: str = betterproto.string_field(9)
    lat: float = betterproto.double_field(10)
    lon: float = betterproto.double_field(11)
    hae: float = betterproto.double_field(12)
    ce: float = betterproto.double_field(13)
    le: float = betterproto.double_field(14)
    detail: "Detail" = betterproto.message_field(15)


@dataclass
class TakControl(betterproto.Message):
    min_proto_version: int = betterproto.uint32_field(1)
    max_proto_version: int = betterproto.uint32_field(2)
    contact_uid: str = betterproto.string_field(3)


@dataclass
class TakMessage(betterproto.Message):
    tak_control: "TakControl" = betterproto.message_field(1)
    cot_event: "CotEvent" = betterproto.message_field(2)
