import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": { "text": text_to_analyze }}
    response = requests.post(url, json = myobj, headers=header)
    response.raise_for_status()
    
    data = json.loads(response.text)
    scores = data['emotionPredictions'][0]['emotion']

    emotions = {
        'anger': scores['anger'],
        'disgust': scores['disgust'],
        'fear': scores['fear'],
        'joy': scores['joy'],
        'sadness': scores['sadness']
    }
    emotions['dominant_emotion'] = max(emotions, key=emotions.get)

    return emotions
