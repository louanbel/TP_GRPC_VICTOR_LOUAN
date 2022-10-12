# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: movie.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bmovie.proto\"\x15\n\x07MovieID\x12\n\n\x02id\x18\x01 \x01(\t\"\x16\n\x05Title\x12\r\n\x05title\x18\x01 \x01(\t\"\x1c\n\x08\x44irector\x12\x10\n\x08\x64irector\x18\x01 \x01(\t\"H\n\tMovieData\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0e\n\x06rating\x18\x02 \x01(\x02\x12\x10\n\x08\x64irector\x18\x03 \x01(\t\x12\n\n\x02id\x18\x04 \x01(\t\"\x07\n\x05\x45mpty2\xfd\x01\n\x05Movie\x12&\n\x0cGetMovieByID\x12\x08.MovieID\x1a\n.MovieData\"\x00\x12\'\n\rGetListMovies\x12\x06.Empty\x1a\n.MovieData\"\x00\x30\x01\x12\'\n\x0fGetMovieByTitle\x12\x06.Title\x1a\n.MovieData\"\x00\x12-\n\x12GetMovieByDirector\x12\t.Director\x1a\n.MovieData\"\x00\x12$\n\x08\x41\x64\x64Movie\x12\n.MovieData\x1a\n.MovieData\"\x00\x12%\n\x0b\x44\x65leteMovie\x12\x08.MovieID\x1a\n.MovieData\"\x00\x62\x06proto3')



_MOVIEID = DESCRIPTOR.message_types_by_name['MovieID']
_TITLE = DESCRIPTOR.message_types_by_name['Title']
_DIRECTOR = DESCRIPTOR.message_types_by_name['Director']
_MOVIEDATA = DESCRIPTOR.message_types_by_name['MovieData']
_EMPTY = DESCRIPTOR.message_types_by_name['Empty']
MovieID = _reflection.GeneratedProtocolMessageType('MovieID', (_message.Message,), {
  'DESCRIPTOR' : _MOVIEID,
  '__module__' : 'movie_pb2'
  # @@protoc_insertion_point(class_scope:MovieID)
  })
_sym_db.RegisterMessage(MovieID)

Title = _reflection.GeneratedProtocolMessageType('Title', (_message.Message,), {
  'DESCRIPTOR' : _TITLE,
  '__module__' : 'movie_pb2'
  # @@protoc_insertion_point(class_scope:Title)
  })
_sym_db.RegisterMessage(Title)

Director = _reflection.GeneratedProtocolMessageType('Director', (_message.Message,), {
  'DESCRIPTOR' : _DIRECTOR,
  '__module__' : 'movie_pb2'
  # @@protoc_insertion_point(class_scope:Director)
  })
_sym_db.RegisterMessage(Director)

MovieData = _reflection.GeneratedProtocolMessageType('MovieData', (_message.Message,), {
  'DESCRIPTOR' : _MOVIEDATA,
  '__module__' : 'movie_pb2'
  # @@protoc_insertion_point(class_scope:MovieData)
  })
_sym_db.RegisterMessage(MovieData)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'movie_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  })
_sym_db.RegisterMessage(Empty)

_MOVIE = DESCRIPTOR.services_by_name['Movie']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MOVIEID._serialized_start=15
  _MOVIEID._serialized_end=36
  _TITLE._serialized_start=38
  _TITLE._serialized_end=60
  _DIRECTOR._serialized_start=62
  _DIRECTOR._serialized_end=90
  _MOVIEDATA._serialized_start=92
  _MOVIEDATA._serialized_end=164
  _EMPTY._serialized_start=166
  _EMPTY._serialized_end=173
  _MOVIE._serialized_start=176
  _MOVIE._serialized_end=429
# @@protoc_insertion_point(module_scope)
