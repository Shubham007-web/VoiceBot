from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List

class ActionFetchInterestRate(Action):
    def name(self) -> Text:
        return "action_fetch_interest_rate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Any, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Logic to fetch interest rate
        interest_rate = "12.5"
        dispatcher.utter_message(text=f"The current interest rate is {interest_rate}%.")
        return []

class ActionConfirmTenure(Action):
    def name(self) -> Text:
        return "action_confirm_tenure"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Any, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        tenure = tracker.get_slot("tenure")  # Fetch tenure from user input or slot
        dispatcher.utter_message(
            text=f"You have selected {tenure} months. Shall I proceed with the EMI conversion?"
        )
        return []


