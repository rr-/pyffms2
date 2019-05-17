# Based on file generated by ctypeslib scripts.
# h2xml ffms.h -o ffms.xml && xml2py ffms.xml -o ffms.py -l libffms2.so

import os
from ctypes import *  # @UnusedWildImport

from .get_library import get_library

lib = get_library(
    "ffms2",
    win_format="{}.dll",
    win64_format=["{}-x64.dll", "{}.dll"],
    win_class_name="WinDLL",
)

FFMS_VERSION = (2 << 24) | (17 << 16) | (3 << 8) | 0
FUNCTYPE = WINFUNCTYPE if os.name == "nt" else CFUNCTYPE
STRING = c_char_p


class FFMS_ErrorInfo(Structure):
    pass


FFMS_ErrorInfo._fields_ = [
    ("ErrorType", c_int),
    ("SubType", c_int),
    ("BufferSize", c_int),
    ("Buffer", STRING),
]


class FFMS_VideoSource(Structure):
    pass


FFMS_VideoSource._fields_ = []


class FFMS_AudioSource(Structure):
    pass


FFMS_AudioSource._fields_ = []


class FFMS_Indexer(Structure):
    pass


FFMS_Indexer._fields_ = []


class FFMS_Index(Structure):
    pass


FFMS_Index._fields_ = []


class FFMS_Track(Structure):
    pass


FFMS_Track._fields_ = []

# values for enumeration 'FFMS_Errors'
FFMS_Errors = c_int  # enum

# values for enumeration 'FFMS_Sources'
FFMS_Sources = c_int  # enum

# values for enumeration 'FFMS_CPUFeatures'
FFMS_CPUFeatures = c_int  # enum

# values for enumeration 'FFMS_SeekMode'
FFMS_SeekMode = c_int  # enum

# values for enumeration 'FFMS_IndexErrorHandling'
FFMS_IndexErrorHandling = c_int  # enum

# values for enumeration 'FFMS_TrackType'
FFMS_TrackType = c_int  # enum

# values for enumeration 'FFMS_SampleFormat'
FFMS_SampleFormat = c_int  # enum

# values for enumeration 'FFMS_AudioChannel'
FFMS_AudioChannel = c_int  # enum

# values for enumeration 'FFMS_Resizers'
FFMS_Resizers = c_int  # enum

# values for enumeration 'FFMS_AudioDelayModes'
FFMS_AudioDelayModes = c_int  # enum

# values for enumeration 'FFMS_ColorSpaces'
FFMS_ColorSpaces = c_int  # enum

# values for enumeration 'FFMS_ColorRanges'
FFMS_ColorRanges = c_int  # enum


class FFMS_Frame(Structure):
    pass


uint8_t = c_uint8
FFMS_Frame._fields_ = [
    ("Data", POINTER(uint8_t) * 4),
    ("Linesize", c_int * 4),
    ("EncodedWidth", c_int),
    ("EncodedHeight", c_int),
    ("EncodedPixelFormat", c_int),
    ("ScaledWidth", c_int),
    ("ScaledHeight", c_int),
    ("ConvertedPixelFormat", c_int),
    ("KeyFrame", c_int),
    ("RepeatPict", c_int),
    ("InterlacedFrame", c_int),
    ("TopFieldFirst", c_int),
    ("PictType", c_char),
    ("ColorSpace", c_int),
    ("ColorRange", c_int),
]


class FFMS_TrackTimeBase(Structure):
    pass


int64_t = c_int64
FFMS_TrackTimeBase._fields_ = [("Num", int64_t), ("Den", int64_t)]


class FFMS_FrameInfo(Structure):
    pass


FFMS_FrameInfo._fields_ = [
    ("PTS", int64_t),
    ("RepeatPict", c_int),
    ("KeyFrame", c_int),
]


class FFMS_VideoProperties(Structure):
    pass


FFMS_VideoProperties._fields_ = [
    ("FPSDenominator", c_int),
    ("FPSNumerator", c_int),
    ("RFFDenominator", c_int),
    ("RFFNumerator", c_int),
    ("NumFrames", c_int),
    ("SARNum", c_int),
    ("SARDen", c_int),
    ("CropTop", c_int),
    ("CropBottom", c_int),
    ("CropLeft", c_int),
    ("CropRight", c_int),
    ("TopFieldFirst", c_int),
    ("ColorSpace", c_int),
    ("ColorRange", c_int),
    ("FirstTime", c_double),
    ("LastTime", c_double),
]


class FFMS_AudioProperties(Structure):
    pass


FFMS_AudioProperties._fields_ = [
    ("SampleFormat", c_int),
    ("SampleRate", c_int),
    ("BitsPerSample", c_int),
    ("Channels", c_int),
    ("ChannelLayout", int64_t),
    ("NumSamples", int64_t),
    ("FirstTime", c_double),
    ("LastTime", c_double),
]
TIndexCallback = FUNCTYPE(c_int, int64_t, int64_t, c_void_p)

FFMS_Init = lib.FFMS_Init
FFMS_Init.restype = None
FFMS_Init.argtypes = [c_int, c_int]
FFMS_GetVersion = lib.FFMS_GetVersion
FFMS_GetVersion.restype = c_int
FFMS_GetVersion.argtypes = []
FFMS_GetLogLevel = lib.FFMS_GetLogLevel
FFMS_GetLogLevel.restype = c_int
FFMS_GetLogLevel.argtypes = []
FFMS_SetLogLevel = lib.FFMS_SetLogLevel
FFMS_SetLogLevel.restype = None
FFMS_SetLogLevel.argtypes = [c_int]
FFMS_CreateVideoSource = lib.FFMS_CreateVideoSource
FFMS_CreateVideoSource.restype = POINTER(FFMS_VideoSource)
FFMS_CreateVideoSource.argtypes = [
    STRING,
    c_int,
    POINTER(FFMS_Index),
    c_int,
    c_int,
    POINTER(FFMS_ErrorInfo),
]
FFMS_CreateAudioSource = lib.FFMS_CreateAudioSource
FFMS_CreateAudioSource.restype = POINTER(FFMS_AudioSource)
FFMS_CreateAudioSource.argtypes = [
    STRING,
    c_int,
    POINTER(FFMS_Index),
    c_int,
    POINTER(FFMS_ErrorInfo),
]
FFMS_DestroyVideoSource = lib.FFMS_DestroyVideoSource
FFMS_DestroyVideoSource.restype = None
FFMS_DestroyVideoSource.argtypes = [POINTER(FFMS_VideoSource)]
FFMS_DestroyAudioSource = lib.FFMS_DestroyAudioSource
FFMS_DestroyAudioSource.restype = None
FFMS_DestroyAudioSource.argtypes = [POINTER(FFMS_AudioSource)]
FFMS_GetVideoProperties = lib.FFMS_GetVideoProperties
FFMS_GetVideoProperties.restype = POINTER(FFMS_VideoProperties)
FFMS_GetVideoProperties.argtypes = [POINTER(FFMS_VideoSource)]
FFMS_GetAudioProperties = lib.FFMS_GetAudioProperties
FFMS_GetAudioProperties.restype = POINTER(FFMS_AudioProperties)
FFMS_GetAudioProperties.argtypes = [POINTER(FFMS_AudioSource)]
FFMS_GetFrame = lib.FFMS_GetFrame
FFMS_GetFrame.restype = POINTER(FFMS_Frame)
FFMS_GetFrame.argtypes = [
    POINTER(FFMS_VideoSource),
    c_int,
    POINTER(FFMS_ErrorInfo),
]
FFMS_GetFrameByTime = lib.FFMS_GetFrameByTime
FFMS_GetFrameByTime.restype = POINTER(FFMS_Frame)
FFMS_GetFrameByTime.argtypes = [
    POINTER(FFMS_VideoSource),
    c_double,
    POINTER(FFMS_ErrorInfo),
]
FFMS_GetAudio = lib.FFMS_GetAudio
FFMS_GetAudio.restype = c_int
FFMS_GetAudio.argtypes = [
    POINTER(FFMS_AudioSource),
    c_void_p,
    int64_t,
    int64_t,
    POINTER(FFMS_ErrorInfo),
]
try:
    FFMS_SetOutputFormatV2 = lib.FFMS_SetOutputFormatV2
    FFMS_SetOutputFormatV2.restype = c_int
    FFMS_SetOutputFormatV2.argtypes = [
        POINTER(FFMS_VideoSource),
        POINTER(c_int),
        c_int,
        c_int,
        c_int,
        POINTER(FFMS_ErrorInfo),
    ]
except AttributeError:
    FFMS_SetOutputFormatV2 = None
    FFMS_SetOutputFormatV = lib.FFMS_SetOutputFormatV
    FFMS_SetOutputFormatV.restype = c_int
    FFMS_SetOutputFormatV.argtypes = [
        POINTER(FFMS_VideoSource),
        int64_t,
        c_int,
        c_int,
        c_int,
        POINTER(FFMS_ErrorInfo),
    ]
FFMS_ResetOutputFormatV = lib.FFMS_ResetOutputFormatV
FFMS_ResetOutputFormatV.restype = None
FFMS_ResetOutputFormatV.argtypes = [POINTER(FFMS_VideoSource)]
try:
    FFMS_SetInputFormatV = lib.FFMS_SetInputFormatV
    FFMS_SetInputFormatV.restype = c_int
    FFMS_SetInputFormatV.argtypes = [
        POINTER(FFMS_VideoSource),
        c_int,
        c_int,
        c_int,
        POINTER(FFMS_ErrorInfo),
    ]
    FFMS_ResetInputFormatV = lib.FFMS_ResetInputFormatV
    FFMS_ResetInputFormatV.restype = None
    FFMS_ResetInputFormatV.argtypes = [POINTER(FFMS_VideoSource)]
except AttributeError:
    FFMS_SetInputFormatV = FFMS_ResetInputFormatV = None
FFMS_DestroyIndex = lib.FFMS_DestroyIndex
FFMS_DestroyIndex.restype = None
FFMS_DestroyIndex.argtypes = [POINTER(FFMS_Index)]
FFMS_GetFirstTrackOfType = lib.FFMS_GetFirstTrackOfType
FFMS_GetFirstTrackOfType.restype = c_int
FFMS_GetFirstTrackOfType.argtypes = [
    POINTER(FFMS_Index),
    c_int,
    POINTER(FFMS_ErrorInfo),
]
FFMS_TrackIndexSettings = lib.FFMS_TrackIndexSettings
FFMS_TrackIndexSettings.restype = None
FFMS_TrackIndexSettings.argtypes = [POINTER(FFMS_Indexer), c_int, c_int, c_int]
FFMS_GetFirstIndexedTrackOfType = lib.FFMS_GetFirstIndexedTrackOfType
FFMS_GetFirstIndexedTrackOfType.restype = c_int
FFMS_GetFirstIndexedTrackOfType.argtypes = [
    POINTER(FFMS_Index),
    c_int,
    POINTER(FFMS_ErrorInfo),
]
FFMS_GetNumTracks = lib.FFMS_GetNumTracks
FFMS_GetNumTracks.restype = c_int
FFMS_GetNumTracks.argtypes = [POINTER(FFMS_Index)]
FFMS_GetNumTracksI = lib.FFMS_GetNumTracksI
FFMS_GetNumTracksI.restype = c_int
FFMS_GetNumTracksI.argtypes = [POINTER(FFMS_Indexer)]
FFMS_GetTrackType = lib.FFMS_GetTrackType
FFMS_GetTrackType.restype = c_int
FFMS_GetTrackType.argtypes = [POINTER(FFMS_Track)]
FFMS_GetTrackTypeI = lib.FFMS_GetTrackTypeI
FFMS_GetTrackTypeI.restype = c_int
FFMS_GetTrackTypeI.argtypes = [POINTER(FFMS_Indexer), c_int]
FFMS_GetCodecNameI = lib.FFMS_GetCodecNameI
FFMS_GetCodecNameI.restype = STRING
FFMS_GetCodecNameI.argtypes = [POINTER(FFMS_Indexer), c_int]
FFMS_GetFormatNameI = lib.FFMS_GetFormatNameI
FFMS_GetFormatNameI.restype = STRING
FFMS_GetFormatNameI.argtypes = [POINTER(FFMS_Indexer)]
FFMS_GetNumFrames = lib.FFMS_GetNumFrames
FFMS_GetNumFrames.restype = c_int
FFMS_GetNumFrames.argtypes = [POINTER(FFMS_Track)]
FFMS_GetFrameInfo = lib.FFMS_GetFrameInfo
FFMS_GetFrameInfo.restype = POINTER(FFMS_FrameInfo)
FFMS_GetFrameInfo.argtypes = [POINTER(FFMS_Track), c_int]
FFMS_GetTrackFromIndex = lib.FFMS_GetTrackFromIndex
FFMS_GetTrackFromIndex.restype = POINTER(FFMS_Track)
FFMS_GetTrackFromIndex.argtypes = [POINTER(FFMS_Index), c_int]
FFMS_GetTrackFromVideo = lib.FFMS_GetTrackFromVideo
FFMS_GetTrackFromVideo.restype = POINTER(FFMS_Track)
FFMS_GetTrackFromVideo.argtypes = [POINTER(FFMS_VideoSource)]
FFMS_GetTrackFromAudio = lib.FFMS_GetTrackFromAudio
FFMS_GetTrackFromAudio.restype = POINTER(FFMS_Track)
FFMS_GetTrackFromAudio.argtypes = [POINTER(FFMS_AudioSource)]
FFMS_GetTimeBase = lib.FFMS_GetTimeBase
FFMS_GetTimeBase.restype = POINTER(FFMS_TrackTimeBase)
FFMS_GetTimeBase.argtypes = [POINTER(FFMS_Track)]
FFMS_WriteTimecodes = lib.FFMS_WriteTimecodes
FFMS_WriteTimecodes.restype = c_int
FFMS_WriteTimecodes.argtypes = [
    POINTER(FFMS_Track),
    STRING,
    POINTER(FFMS_ErrorInfo),
]
FFMS_SetProgressCallback = lib.FFMS_SetProgressCallback
FFMS_SetProgressCallback.restype = c_int
FFMS_SetProgressCallback.argtypes = [
    POINTER(FFMS_Indexer),
    TIndexCallback,
    c_void_p,
]
FFMS_CreateIndexer = lib.FFMS_CreateIndexer
FFMS_CreateIndexer.restype = POINTER(FFMS_Indexer)
FFMS_CreateIndexer.argtypes = [STRING, POINTER(FFMS_ErrorInfo)]
FFMS_DoIndexing2 = lib.FFMS_DoIndexing2
FFMS_DoIndexing2.restype = POINTER(FFMS_Index)
FFMS_DoIndexing2.argtypes = [
    POINTER(FFMS_Indexer),
    c_int,
    POINTER(FFMS_ErrorInfo),
]
FFMS_CancelIndexing = lib.FFMS_CancelIndexing
FFMS_CancelIndexing.restype = None
FFMS_CancelIndexing.argtypes = [POINTER(FFMS_Indexer)]
FFMS_ReadIndex = lib.FFMS_ReadIndex
FFMS_ReadIndex.restype = POINTER(FFMS_Index)
FFMS_ReadIndex.argtypes = [STRING, POINTER(FFMS_ErrorInfo)]
FFMS_IndexBelongsToFile = lib.FFMS_IndexBelongsToFile
FFMS_IndexBelongsToFile.restype = c_int
FFMS_IndexBelongsToFile.argtypes = [
    POINTER(FFMS_Index),
    STRING,
    POINTER(FFMS_ErrorInfo),
]
FFMS_WriteIndex = lib.FFMS_WriteIndex
FFMS_WriteIndex.restype = c_int
FFMS_WriteIndex.argtypes = [
    STRING,
    POINTER(FFMS_Index),
    POINTER(FFMS_ErrorInfo),
]
FFMS_GetPixFmt = lib.FFMS_GetPixFmt
FFMS_GetPixFmt.restype = c_int
FFMS_GetPixFmt.argtypes = [STRING]

try:
    FFMS_GetErrorHandling = lib.FFMS_GetErrorHandling
    FFMS_GetErrorHandling.restype = c_int
    FFMS_GetErrorHandling.argtypes = [POINTER(FFMS_Index)]
except AttributeError:
    FFMS_GetErrorHandling = None
