# A Dockerized API

An API based on FastAPI for using neural text-to-speech synthesis. The API is designed to be used together with our
[text-to-speech workers](https://github.com/TartuNLP/text-to-speech-worker).

The project is developed by the [NLP research group](https://tartunlp.ai) at the [University of Tartu](https://ut.ee).
Speech synthesis can also be tested in our [web demo](https://www.neurokone.ee/).

## API usage

The API documentation will be available at the `/docs` endpoint when deployed.

To use the API, use the following POST request format:

POST `/v2`

BODY (JSON):

```json
{
    "text": "Tere.",
    "speaker": "mari",
    "speed": 1
}
```

The `speaker` parameter is required and should contain the speaker's name. The `speed` parameter is optional,
and it is a multiplier between `0.5` and `2` compared to normal speed `1`. As a result the API will return audio
in `.wav` format.
