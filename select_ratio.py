class SelectRatioToWH:
    """
    A node generate width and height by select ratio

    """
    def __init__(self):
        self.ratio_list = {
            "1:1":"1024:1024",
            "4:3":"1152:896",
            "3:2":"1216:832",
            "8:5":"1216:768",
            "16:9":"1344:768",
            "21:9":"1536:640",
            "3:4":"896:1152",
            "2:3":"832:1216",
            "5,8":"768:1216",
            "9:16":"768:1344",
            "9:21":"640:1536",
        }
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
        return {"required": {"ratio": (['1:1','4:3','3:2','8:5','16:9','21:9','3:4','2:3','5,8','9:16','9:21'], ),
                            }
                }
        # return {"required": { "radio": (['1:1', '4:3'], ),
        #                     }
        #         }
    
    def select_ratio(self, ratio):
        width_height = self.ratio_list[ratio]
        width = int(width_height.split(":")[0])
        height = int(width_height.split(":")[-1])
        return (width, height)

    RETURN_TYPES = ("INT","INT")
    RETURN_NAMES = ("width","height")

    FUNCTION = "select_ratio"

    CATEGORY = "Width And Height"

if __name__ == "__main__":
    ratio_list = {
            "1:1":"1024:1024",
            "4:3":"1152:896",
            "3:2":"1216:832",
            "8:5":"1216:768",
            "16:9":"1344:768",
            "21:9":"1536:640",
            "3:4":"896:1152",
            "2:3":"832:1216",
            "5,8":"768:1216",
            "9:16":"768:1344",
            "9:21":"640:1536",
        }
    
    def select_ratio(ratio):
        width_height = ratio_list[ratio]
        width = int(width_height.split(":")[0])
        height = int(width_height.split(":")[-1])
        return (width, height)
    
    width, height = select_ratio("16:9")
    print(width, f"{type(width)}")
    print(height, f"{type(height)}")