# A Dockerized API

An API based on FastAPI for using the transformer-based text-to-audio model: [Bark](https://github.com/suno-ai/bark)

The model is from [Suno](https://suno.ai)


## API usage

The API documentation will be available at the `/docs` endpoint when deployed.

To use the API, use the following POST request format:

POST `/predict`

Body (JSON):

```json
{
    "text_prompt": "The text prompt for which we wanna generate the audio"
}
```

To play the audio, send a GET request as:

GET `/predict`

The API returns the audio in `.wav` format.
