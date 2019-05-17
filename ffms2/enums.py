"""FFMS enumerations
"""

FFMS_CH_FRONT_LEFT = 0x1
FFMS_CH_FRONT_RIGHT = 0x2
FFMS_CH_FRONT_CENTER = 0x4
FFMS_CH_LOW_FREQUENCY = 0x8
FFMS_CH_BACK_LEFT = 0x10
FFMS_CH_BACK_RIGHT = 0x20
FFMS_CH_FRONT_LEFT_OF_CENTER = 0x40
FFMS_CH_FRONT_RIGHT_OF_CENTER = 0x80
FFMS_CH_BACK_CENTER = 0x100
FFMS_CH_SIDE_LEFT = 0x200
FFMS_CH_SIDE_RIGHT = 0x400
FFMS_CH_TOP_CENTER = 0x800
FFMS_CH_TOP_FRONT_LEFT = 0x1000
FFMS_CH_TOP_FRONT_CENTER = 0x2000
FFMS_CH_TOP_FRONT_RIGHT = 0x4000
FFMS_CH_TOP_BACK_LEFT = 0x8000
FFMS_CH_TOP_BACK_CENTER = 0x10000
FFMS_CH_TOP_BACK_RIGHT = 0x20000
FFMS_CH_STEREO_LEFT = 0x20000000
FFMS_CH_STEREO_RIGHT = 0x40000000
FFMS_CPU_CAPS_MMX = 0x1
FFMS_CPU_CAPS_MMX2 = 0x2
FFMS_CPU_CAPS_3DNOW = 0x4
FFMS_CPU_CAPS_ALTIVEC = 0x8
FFMS_CPU_CAPS_BFIN = 0x10
FFMS_CPU_CAPS_SSE2 = 0x20
FFMS_CR_UNSPECIFIED = 0x0
FFMS_CR_MPEG = 0x1
FFMS_CR_JPEG = 0x2
FFMS_CS_RGB = 0x0
FFMS_CS_BT709 = 0x1
FFMS_CS_UNSPECIFIED = 0x2
FFMS_CS_FCC = 0x4
FFMS_CS_BT470BG = 0x5
FFMS_CS_SMPTE170M = 0x6
FFMS_CS_SMPTE240M = 0x7
FFMS_DELAY_NO_SHIFT = -0x3
FFMS_DELAY_TIME_ZERO = -0x2
FFMS_DELAY_FIRST_VIDEO_TRACK = -0x1
FFMS_ERROR_SUCCESS = 0x0
FFMS_ERROR_INDEX = 0x1
FFMS_ERROR_INDEXING = 0x2
FFMS_ERROR_POSTPROCESSING = 0x3
FFMS_ERROR_SCALING = 0x4
FFMS_ERROR_DECODING = 0x5
FFMS_ERROR_SEEKING = 0x6
FFMS_ERROR_PARSER = 0x7
FFMS_ERROR_TRACK = 0x8
FFMS_ERROR_WAVE_WRITER = 0x9
FFMS_ERROR_CANCELLED = 0xA
FFMS_ERROR_UNKNOWN = 0x14
FFMS_ERROR_UNSUPPORTED = 0x15
FFMS_ERROR_FILE_READ = 0x16
FFMS_ERROR_FILE_WRITE = 0x17
FFMS_ERROR_NO_FILE = 0x18
FFMS_ERROR_VERSION = 0x19
FFMS_ERROR_ALLOCATION_FAILED = 0x1A
FFMS_ERROR_INVALID_ARGUMENT = 0x1B
FFMS_ERROR_CODEC = 0x1C
FFMS_ERROR_NOT_AVAILABLE = 0x1D
FFMS_ERROR_FILE_MISMATCH = 0x1E
FFMS_ERROR_USER = 0x1F
FFMS_FMT_U8 = 0x0
FFMS_FMT_S16 = 0x1
FFMS_FMT_S32 = 0x2
FFMS_FMT_FLT = 0x3
FFMS_FMT_DBL = 0x4
FFMS_IEH_ABORT = 0x0
FFMS_IEH_CLEAR_TRACK = 0x1
FFMS_IEH_STOP_TRACK = 0x2
FFMS_IEH_IGNORE = 0x3
FFMS_RESIZER_FAST_BILINEAR = 0x1
FFMS_RESIZER_BILINEAR = 0x2
FFMS_RESIZER_BICUBIC = 0x4
FFMS_RESIZER_X = 0x8
FFMS_RESIZER_POINT = 0x10
FFMS_RESIZER_AREA = 0x20
FFMS_RESIZER_BICUBLIN = 0x40
FFMS_RESIZER_GAUSS = 0x80
FFMS_RESIZER_SINC = 0x100
FFMS_RESIZER_LANCZOS = 0x200
FFMS_RESIZER_SPLINE = 0x400
FFMS_SEEK_LINEAR_NO_RW = -0x1
FFMS_SEEK_LINEAR = 0x0
FFMS_SEEK_NORMAL = 0x1
FFMS_SEEK_UNSAFE = 0x2
FFMS_SEEK_AGGRESSIVE = 0x3
FFMS_SOURCE_DEFAULT = 0x0
FFMS_SOURCE_LAVF = 0x1
FFMS_SOURCE_MATROSKA = 0x2
FFMS_SOURCE_HAALIMPEG = 0x4
FFMS_SOURCE_HAALIOGG = 0x8
FFMS_TYPE_UNKNOWN = -0x1
FFMS_TYPE_VIDEO = 0x0
FFMS_TYPE_AUDIO = 0x1
FFMS_TYPE_DATA = 0x2
FFMS_TYPE_SUBTITLE = 0x3
FFMS_TYPE_ATTACHMENT = 0x4
