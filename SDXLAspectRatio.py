# quick node to set SDXL-friendly aspect ratios in 1024^2
# by throttlekitty

class SDXLAspectRatio:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "width": ("INT", {"default": 64, "min": 64, "max": 2048,}),
                "height": ("INT", {"default": 64, "min": 64, "max": 2048}),
                "aspectRatio": ([
                " 512 x 1024",
                " 512 x  768",
                " 512 x  512",
                " 768 x  512",
                "1024 x  512",
                " 768 x  768",
                " ", 
                " 640 x 1536",
                " 704 x 1408",
                " 768 x 1344",
                " 832 x 1216",
                " 896 x 1152",
                "1024 x 1024",
                "1152 x  896", 
                "1216 x  832", 
                "1344 x  768", 
                "1408 x  704", 
                "1536 x  640",
                " ",
                "1280 x 1280",
                "1536 x 1536",
                "1792 x 1792",
                " ",
                "1280 x 3072",
                "1664 x 2432",
                "2048 x 2048",
                "2432 x 1664", 
                "3072 x 1280"],)
            }
        }
    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("Width", "Height")
    FUNCTION = "SDXL_AspectRatio"
    CATEGORY = "image"

    def SDXL_AspectRatio(self, width, height, aspectRatio):
        if aspectRatio == "Manual":
            width, height = width, height
        elif aspectRatio == " 512 x 1024":
            width, height = 512, 1024
        elif aspectRatio == " 512 x  768":
            width, height = 512, 768
        elif aspectRatio == " 512 x  512":
            width, height = 512, 512
        elif aspectRatio == " 768 x  512":
            width, height = 768, 512
        elif aspectRatio == "1024 x  512":
            width, height = 1024, 512
        elif aspectRatio == " 768 x  768":
            width, height = 768, 768
        elif aspectRatio == " 640 x 1536":
            width, height = 640, 1536
        elif aspectRatio == " 704 x 1408":
            width, height = 704, 1408
        elif aspectRatio == " 768 x 1344":
            width, height = 768, 1344
        elif aspectRatio == " 832 x 1216":
            width, height = 832, 1216
        elif aspectRatio == " 896 x 1152":
            width, height = 896, 1152
        elif aspectRatio == "1024 x 1024":
            width, height = 1024, 1024
        elif aspectRatio == "1152 x  896":
            width, height = 1152, 896
        elif aspectRatio == "1216 x  832":
            width, height = 1216, 832
        elif aspectRatio == "1344 x  768":
            width, height = 1344, 768
        elif aspectRatio == "1408 x  704":
            width, height = 1408, 704
        elif aspectRatio == "1536 x  640":
            width, height = 1536, 640
        elif aspectRatio == "1280 x 1280":
            width, height = 1280, 1280
        elif aspectRatio == "1536 x 1536":
            width, height = 1536, 1536
        elif aspectRatio == "1792 x 1792":
            width, height = 1792, 1792
        elif aspectRatio == "1280 x 3072":
            width, height = 1280, 3072
        elif aspectRatio == "1664 x 2432":
            width, height = 1664, 2432
        elif aspectRatio == "2048 x 2048":
            width, height = 2048, 2048
        elif aspectRatio == "2432 x 1664":
            width, height = 2432, 1664
        elif aspectRatio == "3072 x 1280":
            width, height = 3072, 1280
        return(width, height)

NODE_CLASS_MAPPINGS = {
    "SDXLAspectRatio": SDXLAspectRatio
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "SDXLAspectRatio": "SDXL Aspect Ratio"
}