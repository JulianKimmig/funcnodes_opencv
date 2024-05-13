from typing import Optional, Tuple
import cv2
import numpy as np
from .imageformat import OpenCVImageFormat, ImageFormat, NumpyImageFormat
import funcnodes as fn
import math


class ColorCodes(fn.DataEnum):
    GRAY = "GRAY"
    BRG = "BGR"
    RGB = "RGB"
    HSV = "HSV"
    LAB = "LAB"
    YUV = "YUV"
    YCrCb = "YCrCb"
    XYZ = "XYZ"
    HLS = "HLS"
    LUV = "LUV"


@fn.NodeDecorator(
    node_id="cv2.color_convert",
    outputs=[
        {"name": "out", "type": OpenCVImageFormat},
    ],
    default_render_options={"data": {"src": "out"}},
)
def color_convert(
    img: ImageFormat,
    code: ColorCodes = ColorCodes.GRAY,
) -> NumpyImageFormat:
    code = ColorCodes.v(code)
    return NumpyImageFormat(img.to_cv2().to_colorspace(code))


NODE_SHELF = fn.Shelf(
    name="Color Modes",
    nodes=[
        color_convert,
    ],
    description="Nodes for converting between color modes",
    subshelves=[],
)
