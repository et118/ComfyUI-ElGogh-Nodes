from nodes import CLIPTextEncode, EmptyLatentImage, CheckpointLoaderSimple, LoraLoader, VAELoader, KSamplerAdvanced, CLIPSetLastLayer
from server import PromptServer
class ElGoghPositivePrompt(CLIPTextEncode):
    CATEGORY = "El Gogh"
    
class ElGoghNegativePrompt(CLIPTextEncode):
    CATEGORY = "El Gogh"

class ElGoghEmptyLatentImage(EmptyLatentImage):
    CATEGORY = "El Gogh"

class ElGoghCheckpointLoaderSimple(CheckpointLoaderSimple):
    CATEGORY = "El Gogh"

class ElGoghPrimaryLoraLoader(LoraLoader):
    CATEGORY = "El Gogh"

class ElGoghSecondaryLoraLoader(LoraLoader):
    CATEGORY = "El Gogh"

class ElGoghTertiaryLoraLoader(LoraLoader):
    CATEGORY = "El Gogh"

class ElGoghVAELoader(VAELoader):
    CATEGORY = "El Gogh"

class ElGoghKSamplerAdvanced(KSamplerAdvanced):
    CATEGORY = "El Gogh"

class ElGoghCLIPSetLastLayer(CLIPSetLastLayer):
    CATEGORY = "El Gogh"

class ElGoghSendWebsocketNSFWBool():
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "nsfw": ("BOOLEAN",{"defaultInput": True})
            },
        }

    RETURN_TYPES = ()
    RETURN_NAMES = ()
    FUNCTION = "sendMessage"
    CATEGORY = "El Gogh"
    OUTPUT_NODE = True

    def sendMessage(self, nsfw):
        server = PromptServer.instance
        server.send_sync("ElGogh-NSFW",nsfw)
        return {}

NODE_CLASS_MAPPINGS = {
    "ElGoghPositivePrompt": ElGoghPositivePrompt,
    "ElGoghNegativePrompt": ElGoghNegativePrompt,
    "ElGoghEmptyLatentImage": ElGoghEmptyLatentImage,
    "ElGoghCheckpointLoaderSimple": ElGoghCheckpointLoaderSimple,
    "ElGoghPrimaryLoraLoader": ElGoghPrimaryLoraLoader,
    "ElGoghSecondaryLoraLoader": ElGoghSecondaryLoraLoader,
    "ElGoghTertiaryLoraLoader": ElGoghTertiaryLoraLoader,
    "ElGoghVAELoader": ElGoghVAELoader,
    "ElGoghKSamplerAdvanced": ElGoghKSamplerAdvanced,
    "ElGoghCLIPSetLastLayer": ElGoghCLIPSetLastLayer,
    "ElGoghSendWebsocketNSFWBool": ElGoghSendWebsocketNSFWBool
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ElGoghPositivePrompt": "[El Gogh] Text Encode (Positive Prompt)",
    "ElGoghNegativePrompt": "[El Gogh] Text Encode (Negative Prompt)",
    "ElGoghEmptyLatentImage": "[El Gogh] Empty Latent Image",
    "ElGoghCheckpointLoaderSimple": "[El Gogh] Load Checkpoint",
    "ElGoghPrimaryLoraLoader": "[El Gogh] Primary Load Lora",
    "ElGoghSecondaryLoraLoader": "[El Gogh] Secondary Load Lora",
    "ElGoghTertiaryLoraLoader": "[El Gogh] Tertiary Load Lora",
    "ElGoghVAELoader": "[El Gogh] Load VAE",
    "ElGoghKSamplerAdvanced": "[El Gogh] KSampler (Advanced)",
    "ElGoghCLIPSetLastLayer": "[El Gogh] CLIP Set Last Layer",
    "ElGoghSendWebsocketNSFWBool": "[El Gogh] Send Websocket NSFW Bool"
}