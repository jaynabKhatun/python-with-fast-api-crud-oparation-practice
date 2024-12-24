from bson import objectid


def create_feedback(feedback_data: dict) -> dict:
    meal_id = feedback_data.get("mealId")
    if not objectid.isValid(meal_id):
        raise ValueError("Invalid meal ID")
