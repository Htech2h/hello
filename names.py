allergies = input("Do you have any food allergies please list them separated by commas. Otherwise, enter 'none': ")
health_goal = input("What health goal are you trying to achieve? Enter 'weight loss', 'muscle gain', 'heart health', or 'none': ")
MEALS = [
    {
        "name": "Grilled chicken with vegetables",
        "ingredients": ["chicken breast", "asparagus", "bell pepper", "olive oil"],
        "calories": 400,
        "protein": 40,
        "carbs": 20,
        "fat": 20,
        "allergens": ["none"]
    },
    {
        "name": "Quinoa and black bean bowl",
        "ingredients": ["quinoa", "black beans", "avocado", "tomato", "cilantro"],
        "calories": 450,
        "protein": 20,
        "carbs": 60,
        "fat": 15,
        "allergens": ["none"]
    },
    {
        "name": "Salmon with sweet potato and broccoli",
        "ingredients": ["salmon fillet", "sweet potato", "broccoli", "butter"],
        "calories": 500,
        "protein": 30,
        "carbs": 40,
        "fat": 25,
        "allergens": ["none"]
    }
]

filtered_meals = []
for meal in MEALS:
    if health_goal.lower() == "weight loss" and meal["calories"] > 400:
        continue
    if health_goal.lower() == "muscle gain" and meal["calories"] < 30:
        continue
    if health_goal.lower() == "heart health" and meal["calories"] > 10:
        continue
    filtered_meals.append(meal)
    break
print(filtered_meals)

