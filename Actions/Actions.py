from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionGreet(Action):

    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello! How can I assist 
you today?")

        return []

class ActionGoodbye(Action):

    def name(self) -> Text:
        return "action_goodbye"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Goodbye! Have a great 
day!")

        return []

class ActionTime(Action):

    def name(self) -> Text:
        return "action_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        from datetime import datetime

        time_now = datetime.now().strftime("%H:%M:%S")

        dispatcher.utter_message(text=f"The current time is 
{time_now}")

        return []

class ActionCalculation(Action):

    def name(self) -> Text:
        return "action_calculation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        import math

        expression = tracker.latest_message['text']

        try:
            result = eval(expression)
            if isinstance(result, float):
                result = round(result, 2)
            dispatcher.utter_message(text=f"The answer is 
{result}")
        except:
            dispatcher.utter_message(text="I'm sorry, I couldn't 
perform that calculation.")

        return []
