import logging
from logging.handlers import RotatingFileHandler
from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List

# Configure logging
logger = logging.getLogger("voicebot")
handler = RotatingFileHandler("logs/voicebot.log", maxBytes=5000000, backupCount=3)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

class ActionFetchInterestRate(Action):
    def name(self) -> Text:
        return "action_fetch_interest_rate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Any, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            # Logic to fetch interest rate
            interest_rate = "12.5"
            dispatcher.utter_message(text=f"The current interest rate is {interest_rate}%.")
            logger.info("Fetched interest rate successfully.")
        except Exception as e:
            logger.error(f"Error fetching interest rate: {e}")
            dispatcher.utter_message(text="Sorry, I couldn't fetch the interest rate right now.")
        return []

class ActionConfirmTenure(Action):
    def name(self) -> Text:
        return "action_confirm_tenure"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Any, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            # Fetch tenure from user input or slot
            tenure = tracker.get_slot("tenure")
            if tenure:
                dispatcher.utter_message(
                    text=f"You have selected {tenure} months. Shall I proceed with the EMI conversion?"
                )
                logger.info(f"User selected tenure: {tenure} months.")
            else:
                dispatcher.utter_message(
                    text="It seems I didn't get the tenure. Can you please specify again?"
                )
                logger.warning("Tenure slot is empty.")
        except Exception as e:
            logger.error(f"Error confirming tenure: {e}")
            dispatcher.utter_message(text="Sorry, I couldn't process your request.")
        return []
