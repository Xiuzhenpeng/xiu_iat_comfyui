import math

class OneStringToList:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "string": ('STRING', {"forceInput": True}),
                "string_symbol": ("STRING", {
                    "default": ",",
                    "lazy": True
                }),
            },
        }

    RETURN_TYPES = ("LIST",)

    FUNCTION = "convert"

    OUTPUT_NODE = False
    CATEGORY = "Xiu"
    DESCRIPTION = "将一个使用英文逗号分隔的string转换为list"

    def convert(self, string:str, string_symbol):
        list = []
        for i in range(0, len(string.split(string_symbol))):
            list.append(i)
        print(list)
        print(type(list))
        return list

class GetStringFromList:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "list": ('LIST', {"forceInput": True}),
                "index": ("INT", {
                    "default": 0, 
                    "min": -1000, #Minimum value
                    "max": 1000, #Maximum value
                    "step": 1, #Slider's step
                    "display": "number", # Cosmetic only: display as "number" or "slider"
                    # "lazy": True # Will only be evaluated if check_lazy_status requires it
                }),
            },
        }

    RETURN_TYPES = ("STRING",)

    FUNCTION = "main"

    CATEGORY = "Xiu/List"
    DESCRIPTION = "使用索引提取列表中的元素"

    def main(self, list, index):
        # print(type(list))
        # print(type(index))
        # print(list)
        # print(index)
        output = list[index]
        # print(output)
        return (output,)

class GetIntFromList:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "list": ('LIST', {"forceInput": True}),
                "index": ("INT", {
                    "default": 0, 
                    "min": -1000, #Minimum value
                    "max": 1000, #Maximum value
                    "step": 1, #Slider's step
                    "display": "number", # Cosmetic only: display as "number" or "slider"
                }),
            },
        }

    RETURN_TYPES = ("INT",)

    FUNCTION = "main"

    CATEGORY = "Xiu/List"
    DESCRIPTION = "使用索引提取列表中的元素, 并尝试将字符串转换为INT"

    def main(self, list, index):
        output = list[index]
        if isinstance(output, str):
            if output.isdigit():
                output = int(output)
                print("success to tran input from str to int")
        else:
            print("file to tran input from str to int")
        return (output,)
    
class BagelResizeImageSize:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "width": ('INT', {"forceInput": True}),
                "height": ('INT', {"forceInput": True}),
            },
        }

    RETURN_TYPES = ("INT","INT")
    RETURN_NAMES = ("width","height")

    FUNCTION = "resize_with_constraints"

    CATEGORY = "Xiu/Size"
    DESCRIPTION = "根据长短边及最大像素限制调整图片尺寸"

    def resize_with_constraints(
        self,
        width: int,
        height: int,
        max_size: int = 1024,
        min_size: int = 512,
        stride: int = 16,
        max_pixels: int = 14 * 14 * 9 * 1024,
    ):
        # 原始宽高
        # orig_w, orig_h = width, height

        # 先计算缩放比例，使长边不超过 max_size，短边不小于 min_size
        scale_w = max_size / width
        scale_h = max_size / height
        scale_max = min(scale_w, scale_h)

        scale_w = min_size / width
        scale_h = min_size / height
        scale_min = max(scale_w, scale_h)

        scale = max(scale_min, min(scale_max, 1.0))  # 避免无限放大或缩小

        new_w = int(round(width * scale))
        new_h = int(round(height * scale))

        # 对齐到 stride
        new_w = int(math.floor(new_w / stride)) * stride
        new_h = int(math.floor(new_h / stride)) * stride

        # 检查最大像素限制
        while new_w * new_h > max_pixels:
            new_w = new_w - stride
            new_h = new_h - stride

        return (new_w, new_h,)

class Example:
    """
    A example node

    Class methods
    -------------
    INPUT_TYPES (dict):
        Tell the main program input parameters of nodes.
    IS_CHANGED:
        optional method to control when the node is re executed.

    Attributes
    ----------
    RETURN_TYPES (`tuple`):
        The type of each element in the output tuple.
    RETURN_NAMES (`tuple`):
        Optional: The name of each output in the output tuple.
    FUNCTION (`str`):
        The name of the entry-point method. For example, if `FUNCTION = "execute"` then it will run Example().execute()
    OUTPUT_NODE ([`bool`]):
        If this node is an output node that outputs a result/image from the graph. The SaveImage node is an example.
        The backend iterates on these output nodes and tries to execute all their parents if their parent graph is properly connected.
        Assumed to be False if not present.
    CATEGORY (`str`):
        The category the node should appear in the UI.
    DEPRECATED (`bool`):
        Indicates whether the node is deprecated. Deprecated nodes are hidden by default in the UI, but remain
        functional in existing workflows that use them.
    EXPERIMENTAL (`bool`):
        Indicates whether the node is experimental. Experimental nodes are marked as such in the UI and may be subject to
        significant changes or removal in future versions. Use with caution in production workflows.
    execute(s) -> tuple || None:
        The entry point method. The name of this method must be the same as the value of property `FUNCTION`.
        For example, if `FUNCTION = "execute"` then this method's name must be `execute`, if `FUNCTION = "foo"` then it must be `foo`.
    """
    def __init__(self):
        pass
        
    @classmethod
    def INPUT_TYPES(s):
        """
            Return a dictionary which contains config for all input fields.
            Some types (string): "MODEL", "VAE", "CLIP", "CONDITIONING", "LATENT", "IMAGE", "INT", "STRING", "FLOAT".
            Input types "INT", "STRING" or "FLOAT" are special values for fields on the node.
            The type can be a list for selection.

            Returns: `dict`:
                - Key input_fields_group (`string`): Can be either required, hidden or optional. A node class must have property `required`
                - Value input_fields (`dict`): Contains input fields config:
                    * Key field_name (`string`): Name of a entry-point method's argument
                    * Value field_config (`tuple`):
                        + First value is a string indicate the type of field or a list for selection.
                        + Second value is a config for type "INT", "STRING" or "FLOAT".
        """
        return {
            "required": {
                "image": ("IMAGE",),
                "int_field": ("INT", {
                    "default": 0, 
                    "min": 0, #Minimum value
                    "max": 4096, #Maximum value
                    "step": 64, #Slider's step
                    "display": "number", # Cosmetic only: display as "number" or "slider"
                    "lazy": True # Will only be evaluated if check_lazy_status requires it
                }),
                "float_field": ("FLOAT", {
                    "default": 1.0,
                    "min": 0.0,
                    "max": 10.0,
                    "step": 0.01,
                    "round": 0.001, #The value representing the precision to round to, will be set to the step value by default. Can be set to False to disable rounding.
                    "display": "number",
                    "lazy": True
                }),
                "print_to_screen": (["enable", "disable"],),
                "string_field": ("STRING", {
                    "multiline": False, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": "Hello World!",
                    "lazy": True
                }),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    #RETURN_NAMES = ("image_output_name",)

    FUNCTION = "test"

    #OUTPUT_NODE = False

    CATEGORY = "Example"

    def check_lazy_status(self, image, string_field, int_field, float_field, print_to_screen):
        """
            Return a list of input names that need to be evaluated.

            This function will be called if there are any lazy inputs which have not yet been
            evaluated. As long as you return at least one field which has not yet been evaluated
            (and more exist), this function will be called again once the value of the requested
            field is available.

            Any evaluated inputs will be passed as arguments to this function. Any unevaluated
            inputs will have the value None.
        """
        if print_to_screen == "enable":
            return ["int_field", "float_field", "string_field"]
        else:
            return []

    def test(self, image, string_field, int_field, float_field, print_to_screen):
        if print_to_screen == "enable":
            print(f"""Your input contains:
                string_field aka input text: {string_field}
                int_field: {int_field}
                float_field: {float_field}
            """)
        #do some processing on the image, in this example I just invert it
        image = 1.0 - image
        return (image,)

    """
        The node will always be re executed if any of the inputs change but
        this method can be used to force the node to execute again even when the inputs don't change.
        You can make this node return a number or a string. This value will be compared to the one returned the last time the node was
        executed, if it is different the node will be executed again.
        This method is used in the core repo for the LoadImage node where they return the image hash as a string, if the image hash
        changes between executions the LoadImage node is executed again.
    """
    #@classmethod
    #def IS_CHANGED(s, image, string_field, int_field, float_field, print_to_screen):
    #    return ""

# Set the web directory, any .js file in that directory will be loaded by the frontend as a frontend extension
# WEB_DIRECTORY = "./somejs"


# Add custom API routes, using router
# from aiohttp import web
# from server import PromptServer

# @PromptServer.instance.routes.get("/hello")
# async def get_hello(request):
#     return web.json_response("hello")


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    # "OneStringToList": OneStringToList,
    "GetStringFromList": GetStringFromList,
    "GetIntFromList": GetIntFromList,
    "BagelResizeImageSize": BagelResizeImageSize,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    # "OneStringToList": "OneStringToList Node",
    "GetStringFromList": "GetStringFromList Node",
    "GetIntFromList": "GetIntFromList Node",
    "BagelResizeImageSize": "BagelResizeImageSize Node",
}
