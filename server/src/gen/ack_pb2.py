# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ack.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ack.proto',
  package='proto',
  serialized_pb=_b('\n\tack.proto\x12\x05proto\"T\n\x03\x41\x63k\x12!\n\x06status\x18\x01 \x02(\x0e\x32\x11.proto.Ack.Status\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x19\n\x06Status\x12\x06\n\x02OK\x10\x01\x12\x07\n\x03NOK\x10\x02\x42\x1a\n\x0eifi.iagl.protoB\x08\x41\x63kProto')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_ACK_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='proto.Ack.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOK', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=79,
  serialized_end=104,
)
_sym_db.RegisterEnumDescriptor(_ACK_STATUS)


_ACK = _descriptor.Descriptor(
  name='Ack',
  full_name='proto.Ack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='proto.Ack.status', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='proto.Ack.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ACK_STATUS,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=104,
)

_ACK.fields_by_name['status'].enum_type = _ACK_STATUS
_ACK_STATUS.containing_type = _ACK
DESCRIPTOR.message_types_by_name['Ack'] = _ACK

Ack = _reflection.GeneratedProtocolMessageType('Ack', (_message.Message,), dict(
  DESCRIPTOR = _ACK,
  __module__ = 'ack_pb2'
  # @@protoc_insertion_point(class_scope:proto.Ack)
  ))
_sym_db.RegisterMessage(Ack)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\016ifi.iagl.protoB\010AckProto'))
# @@protoc_insertion_point(module_scope)
