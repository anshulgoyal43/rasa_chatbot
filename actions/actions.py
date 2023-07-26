# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import requests

class ActionStoreQuestion(Action):

    def name(self) -> Text:
        return "action_store_question"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return []
        question = tracker.latest_message.get('text')
        url = "http://127.0.0.1:8080/qa"
        data = {
            "question": question,
            "answer":"",
            "seen": 0
        }
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print("Question added successfully")
        else:
            print("Error: ", response.text)

        # Save the question to questions.txt
        # file_path = "C:/Users/binsuld/Downloads/chatbot/data/questions.txt"
        # with open(file_path, 'a') as file:
            # file.write(question + '\n')

        # dispatcher.utter_message(text="Hello World!")

        return []
