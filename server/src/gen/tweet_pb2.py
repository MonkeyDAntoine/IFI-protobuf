# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tweet.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import user_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tweet.proto',
  package='proto',
  serialized_pb=_b('\n\x0btweet.proto\x12\x05proto\x1a\nuser.proto\"g\n\x05Tweet\x12\x1b\n\x06sender\x18\x01 \x02(\x0b\x32\x0b.proto.User\x12\x1d\n\x08receiver\x18\x02 \x01(\x0b\x32\x0b.proto.User\x12\x11\n\ttimestamp\x18\x03 \x02(\x01\x12\x0f\n\x07message\x18\x04 \x02(\tB\x1c\n\x0eifi.iagl.protoB\nTweetProto')
  ,
  dependencies=[user_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_TWEET = _descriptor.Descriptor(
  name='Tweet',
  full_name='proto.Tweet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sender', full_name='proto.Tweet.sender', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='receiver', full_name='proto.Tweet.receiver', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='proto.Tweet.timestamp', index=2,
      number=3, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='proto.Tweet.message', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=137,
)

_TWEET.fields_by_name['sender'].message_type = user_pb2._USER
_TWEET.fields_by_name['receiver'].message_type = user_pb2._USER
DESCRIPTOR.message_types_by_name['Tweet'] = _TWEET

Tweet = _reflection.GeneratedProtocolMessageType('Tweet', (_message.Message,), dict(
  DESCRIPTOR = _TWEET,
  __module__ = 'tweet_pb2'
  # @@protoc_insertion_point(class_scope:proto.Tweet)
  ))
_sym_db.RegisterMessage(Tweet)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\016ifi.iagl.protoB\nTweetProto'))
# @@protoc_insertion_point(module_scope)
