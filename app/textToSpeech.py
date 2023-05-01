import base64
import soundfile as sf
import os
from fastapi.responses import FileResponse
from bark import generate_audio, preload_models, SAMPLE_RATE

PATH = "D:\Desktop\StableDiffusionAPI"

async def text2Speech(text_prompt, responses={200:{"description":"text to audio", "content":{"audio/wav":{"example":"no audio available"}}}}):
    
    preload_models()
    audio_array = generate_audio(text_prompt)
    sf.write('audio_from_prompt.wav', audio_array, SAMPLE_RATE)

    with open("audio_from_prompt.wav","rb") as file:
        myObj = base64.b64encode(file.read())

    return {"audio": FileResponse(path=os.path.join(PATH, "audio_from_prompt.wav"), media_type="audio/wav",
                                   filename='audio_from_prompt.wav'),
            "data":text_prompt
           }