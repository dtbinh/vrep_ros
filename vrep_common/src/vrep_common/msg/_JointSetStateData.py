"""autogenerated by genpy from vrep_common/JointSetStateData.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class JointSetStateData(genpy.Message):
  _md5sum = "bd1161cd602435f02e226bb73e4acdb9"
  _type = "vrep_common/JointSetStateData"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """std_msgs/Int32MultiArray handles
std_msgs/UInt8MultiArray setModes
std_msgs/Float32MultiArray values

================================================================================
MSG: std_msgs/Int32MultiArray
# Please look at the MultiArrayLayout message definition for
# documentation on all multiarrays.

MultiArrayLayout  layout        # specification of data layout
int32[]           data          # array of data


================================================================================
MSG: std_msgs/MultiArrayLayout
# The multiarray declares a generic multi-dimensional array of a
# particular data type.  Dimensions are ordered from outer most
# to inner most.

MultiArrayDimension[] dim # Array of dimension properties
uint32 data_offset        # padding bytes at front of data

# Accessors should ALWAYS be written in terms of dimension stride
# and specified outer-most dimension first.
# 
# multiarray(i,j,k) = data[data_offset + dim_stride[1]*i + dim_stride[2]*j + k]
#
# A standard, 3-channel 640x480 image with interleaved color channels
# would be specified as:
#
# dim[0].label  = "height"
# dim[0].size   = 480
# dim[0].stride = 3*640*480 = 921600  (note dim[0] stride is just size of image)
# dim[1].label  = "width"
# dim[1].size   = 640
# dim[1].stride = 3*640 = 1920
# dim[2].label  = "channel"
# dim[2].size   = 3
# dim[2].stride = 3
#
# multiarray(i,j,k) refers to the ith row, jth column, and kth channel.
================================================================================
MSG: std_msgs/MultiArrayDimension
string label   # label of given dimension
uint32 size    # size of given dimension (in type units)
uint32 stride  # stride of given dimension
================================================================================
MSG: std_msgs/UInt8MultiArray
# Please look at the MultiArrayLayout message definition for
# documentation on all multiarrays.

MultiArrayLayout  layout        # specification of data layout
uint8[]           data          # array of data


================================================================================
MSG: std_msgs/Float32MultiArray
# Please look at the MultiArrayLayout message definition for
# documentation on all multiarrays.

MultiArrayLayout  layout        # specification of data layout
float32[]         data          # array of data


"""
  __slots__ = ['handles','setModes','values']
  _slot_types = ['std_msgs/Int32MultiArray','std_msgs/UInt8MultiArray','std_msgs/Float32MultiArray']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       handles,setModes,values

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(JointSetStateData, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.handles is None:
        self.handles = std_msgs.msg.Int32MultiArray()
      if self.setModes is None:
        self.setModes = std_msgs.msg.UInt8MultiArray()
      if self.values is None:
        self.values = std_msgs.msg.Float32MultiArray()
    else:
      self.handles = std_msgs.msg.Int32MultiArray()
      self.setModes = std_msgs.msg.UInt8MultiArray()
      self.values = std_msgs.msg.Float32MultiArray()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      length = len(self.handles.layout.dim)
      buff.write(_struct_I.pack(length))
      for val1 in self.handles.layout.dim:
        _x = val1.label
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1
        buff.write(_struct_2I.pack(_x.size, _x.stride))
      buff.write(_struct_I.pack(self.handles.layout.data_offset))
      length = len(self.handles.data)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(struct.pack(pattern, *self.handles.data))
      length = len(self.setModes.layout.dim)
      buff.write(_struct_I.pack(length))
      for val1 in self.setModes.layout.dim:
        _x = val1.label
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1
        buff.write(_struct_2I.pack(_x.size, _x.stride))
      buff.write(_struct_I.pack(self.setModes.layout.data_offset))
      _x = self.setModes.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.values.layout.dim)
      buff.write(_struct_I.pack(length))
      for val1 in self.values.layout.dim:
        _x = val1.label
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1
        buff.write(_struct_2I.pack(_x.size, _x.stride))
      buff.write(_struct_I.pack(self.values.layout.data_offset))
      length = len(self.values.data)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.values.data))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.handles is None:
        self.handles = std_msgs.msg.Int32MultiArray()
      if self.setModes is None:
        self.setModes = std_msgs.msg.UInt8MultiArray()
      if self.values is None:
        self.values = std_msgs.msg.Float32MultiArray()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.handles.layout.dim = []
      for i in range(0, length):
        val1 = std_msgs.msg.MultiArrayDimension()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.label = str[start:end].decode('utf-8')
        else:
          val1.label = str[start:end]
        _x = val1
        start = end
        end += 8
        (_x.size, _x.stride,) = _struct_2I.unpack(str[start:end])
        self.handles.layout.dim.append(val1)
      start = end
      end += 4
      (self.handles.layout.data_offset,) = _struct_I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.handles.data = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.setModes.layout.dim = []
      for i in range(0, length):
        val1 = std_msgs.msg.MultiArrayDimension()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.label = str[start:end].decode('utf-8')
        else:
          val1.label = str[start:end]
        _x = val1
        start = end
        end += 8
        (_x.size, _x.stride,) = _struct_2I.unpack(str[start:end])
        self.setModes.layout.dim.append(val1)
      start = end
      end += 4
      (self.setModes.layout.data_offset,) = _struct_I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.setModes.data = str[start:end].decode('utf-8')
      else:
        self.setModes.data = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.values.layout.dim = []
      for i in range(0, length):
        val1 = std_msgs.msg.MultiArrayDimension()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.label = str[start:end].decode('utf-8')
        else:
          val1.label = str[start:end]
        _x = val1
        start = end
        end += 8
        (_x.size, _x.stride,) = _struct_2I.unpack(str[start:end])
        self.values.layout.dim.append(val1)
      start = end
      end += 4
      (self.values.layout.data_offset,) = _struct_I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.values.data = struct.unpack(pattern, str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      length = len(self.handles.layout.dim)
      buff.write(_struct_I.pack(length))
      for val1 in self.handles.layout.dim:
        _x = val1.label
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1
        buff.write(_struct_2I.pack(_x.size, _x.stride))
      buff.write(_struct_I.pack(self.handles.layout.data_offset))
      length = len(self.handles.data)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(self.handles.data.tostring())
      length = len(self.setModes.layout.dim)
      buff.write(_struct_I.pack(length))
      for val1 in self.setModes.layout.dim:
        _x = val1.label
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1
        buff.write(_struct_2I.pack(_x.size, _x.stride))
      buff.write(_struct_I.pack(self.setModes.layout.data_offset))
      _x = self.setModes.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.values.layout.dim)
      buff.write(_struct_I.pack(length))
      for val1 in self.values.layout.dim:
        _x = val1.label
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1
        buff.write(_struct_2I.pack(_x.size, _x.stride))
      buff.write(_struct_I.pack(self.values.layout.data_offset))
      length = len(self.values.data)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.values.data.tostring())
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.handles is None:
        self.handles = std_msgs.msg.Int32MultiArray()
      if self.setModes is None:
        self.setModes = std_msgs.msg.UInt8MultiArray()
      if self.values is None:
        self.values = std_msgs.msg.Float32MultiArray()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.handles.layout.dim = []
      for i in range(0, length):
        val1 = std_msgs.msg.MultiArrayDimension()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.label = str[start:end].decode('utf-8')
        else:
          val1.label = str[start:end]
        _x = val1
        start = end
        end += 8
        (_x.size, _x.stride,) = _struct_2I.unpack(str[start:end])
        self.handles.layout.dim.append(val1)
      start = end
      end += 4
      (self.handles.layout.data_offset,) = _struct_I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.handles.data = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.setModes.layout.dim = []
      for i in range(0, length):
        val1 = std_msgs.msg.MultiArrayDimension()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.label = str[start:end].decode('utf-8')
        else:
          val1.label = str[start:end]
        _x = val1
        start = end
        end += 8
        (_x.size, _x.stride,) = _struct_2I.unpack(str[start:end])
        self.setModes.layout.dim.append(val1)
      start = end
      end += 4
      (self.setModes.layout.data_offset,) = _struct_I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.setModes.data = str[start:end].decode('utf-8')
      else:
        self.setModes.data = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.values.layout.dim = []
      for i in range(0, length):
        val1 = std_msgs.msg.MultiArrayDimension()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.label = str[start:end].decode('utf-8')
        else:
          val1.label = str[start:end]
        _x = val1
        start = end
        end += 8
        (_x.size, _x.stride,) = _struct_2I.unpack(str[start:end])
        self.values.layout.dim.append(val1)
      start = end
      end += 4
      (self.values.layout.data_offset,) = _struct_I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.values.data = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_2I = struct.Struct("<2I")
