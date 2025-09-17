"""
ComfyUI-By-xiuzhenpeng
"""
from .xiu_iat import GetStringFromList
from .select_ratio import SelectRatioToWH

NODE_CLASS_MAPPINGS = {
    # "OneStringToList": OneStringToList,
    "GetStringFromList": GetStringFromList,
    "SelectRatioToWH": SelectRatioToWH,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    # "OneStringToList": "OneStringToList Node",
    "GetStringFromList": "GetStringFromList Node",
    "SelectRatioToWH": "Generate Width And Height by Ratio",
}

# Export node mappings for ComfyUI
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]