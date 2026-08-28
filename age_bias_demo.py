import random

# Simulate a simplified AI model that predicts age based on features.
# In reality, this would be a complex neural network.

def predict_age(features):
    # This is a highly simplified model. Real AI uses complex feature extraction.
    # We'll simulate bias by making the 'model' more likely to mispredict
    # for certain simulated 'demographics' (represented by feature values).
    
    # Simulate a 'bias' where features associated with 'older' appearance
    # are sometimes interpreted as younger, and vice-versa, especially
    # if the training data was skewed.
    
    # Let's assume 'feature_skin_smoothness' is a key indicator.
    # Higher value means smoother skin (often associated with youth).
    # Lower value means rougher skin (often associated with age).
    
    # We'll introduce a random element that is amplified by a 'bias factor'.
    # This factor could represent underrepresentation of certain age groups
    # or demographics in the training data.
    
    bias_factor = 1.0
    if features.get('ethnicity') == 'group_A': # Simulate a group that might be underrepresented or misunderstood
        bias_factor = 1.5 # Amplified bias for this group
    elif features.get('ethnicity') == 'group_B':
        bias_factor = 0.8 # Less bias for another group

    # Base prediction based on a hypothetical feature
    base_age = 40 - (features.get('feature_skin_smoothness', 5) * 3) + (features.get('feature_wrinkles', 2) * 5)
    
    # Introduce random error, amplified by bias
    error_magnitude = random.uniform(-5, 5) * bias_factor
    predicted_age = base_age + error_magnitude
    
    # Ensure age is within a reasonable range
    return max(1, min(90, int(predicted_age)))

# --- Demonstration ---

# Simulate data points with varying features and ethnicities
# In a real scenario, these would be actual images and their labels.

# Scenario 1: A person from a well-represented group
person1_features = {
    'feature_skin_smoothness': 7,
    'feature_wrinkles': 1,
    'ethnicity': 'group_C'
}
predicted1 = predict_age(person1_features)
print(f"Person 1 (Group C) - Features: {person1_features}, Predicted Age: {predicted1}")

# Scenario 2: A person from a potentially underrepresented or misunderstood group
person2_features = {
    'feature_skin_smoothness': 6,
    'feature_wrinkles': 2,
    'ethnicity': 'group_A'
}
predicted2 = predict_age(person2_features)
print(f"Person 2 (Group A) - Features: {person2_features}, Predicted Age: {predicted2}")

# Scenario 3: Another person from the same potentially underrepresented group
person3_features = {
    'feature_skin_smoothness': 8,
    'feature_wrinkles': 0,
    'ethnicity': 'group_A'
}
predicted3 = predict_age(person3_features)
print(f"Person 3 (Group A) - Features: {person3_features}, Predicted Age: {predicted3}")

# Scenario 4: A person from another group
person4_features = {
    'feature_skin_smoothness': 4,
    'feature_wrinkles': 4,
    'ethnicity': 'group_B'
}
predicted4 = predict_age(person4_features)
print(f"Person 4 (Group B) - Features: {person4_features}, Predicted Age: {predicted4}")

print("\nNote: The 'bias_factor' simulates how training data imbalances can lead to systematic errors.")
print("Person 2 and 3, despite having similar 'youthful' features, might show more varied or inaccurate predictions due to 'group_A' bias.")
