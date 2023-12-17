from nodes import CLIPTextEncode, EmptyLatentImage, CheckpointLoaderSimple
import folder_paths

class ElGogh_Positive_Prompt:
    @classmethod
    def INPUT_TYPES(s):
        return {"required" : {
            "clip" : ("CLIP", {}),
            "text" : ("STRING", {"multiline": True, "default": "Positive"})
        }}
    
    RETURN_TYPES = ("CONDITIONING",)
    CATEGORY = "ElGogh"
    FUNCTION = "Run"

    def Run(self, clip, text):
        return CLIPTextEncode.encode(None, clip, text)
    
class ElGogh_Negative_Prompt:
    @classmethod
    def INPUT_TYPES(s):
        return {"required" : {
            "clip" : ("CLIP", {}),
            "text" : ("STRING", {"multiline": True, "default": "Negative"})
        }}
    
    RETURN_TYPES = ("CONDITIONING",)
    CATEGORY = "ElGogh"
    FUNCTION = "Run"

    def Run(self, clip, text):
        return CLIPTextEncode.encode(None, clip, text)
    
class ElGogh_Empty_Latent_Image:
    def __init__(self, device="cpu"):
        self.device = device

    @classmethod
    def INPUT_TYPES(s):
        return {"required": { "width": ("INT", {"default": 512, "min": 64, "max": 8192, "step": 8}),
                              "height": ("INT", {"default": 512, "min": 64, "max": 8192, "step": 8}),
                              "batch_size": ("INT", {"default": 1, "min": 1, "max": 64})}}

    RETURN_TYPES = ("LATENT",)
    CATEGORY = "ElGogh"
    FUNCTION = "Run"

    def Run(self, width, height, batch_size=1):
        return EmptyLatentImage.generate(None, width, height, batch_size)

class ElGogh_Checkpoint_Loader_Simple:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": { "ckpt_name": (folder_paths.get_filename_list("checkpoints"), ),
                             }}
    RETURN_TYPES = ("MODEL", "CLIP", "VAE")
    CATEGORY = "ElGogh"
    FUNCTION = "Run"
    
    def Run(self, ckpt_name, output_vae=True, output_clip=True):
        return CheckpointLoaderSimple.load_checkpoint(None, ckpt_name, output_vae, output_clip)

NODE_CLASS_MAPPINGS = {
    "ElGoghPositivePrompt": ElGogh_Positive_Prompt,
    "ElGoghNegativePrompt": ElGogh_Negative_Prompt,
    "ElGoghEmptyLatentImage": ElGogh_Empty_Latent_Image,
    "ElGoghCheckpointLoaderSimple": ElGogh_Checkpoint_Loader_Simple
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ElGoghPositivePrompt": "ElGogh Positive Prompt",
    "ElGoghNegativePrompt": "ElGogh NEGATIVE Prompt",
    "ElGoghEmptyLatentImage": "ElGogh Empty Latent Image",
    "ElGoghCheckpointLoaderSimple": "ElGogh Checkpoint Loader Simple"
}