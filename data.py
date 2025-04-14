import pandas as pd
import random

# Define conditions and their symptoms
conditions_symptoms = {
    "Lower back pain": ["pain in lower back", "stiffness in lower back", "pain radiating to legs", "difficulty bending", "muscle spasms"],
    "Neck pain": ["pain in neck", "stiffness in neck", "headaches", "pain radiating to shoulders", "limited range of motion"],
    "Shoulder impingement": ["pain in shoulder", "difficulty lifting arm", "pain when reaching overhead", "weakness in shoulder"],
    "Knee osteoarthritis": ["pain in knee", "swelling in knee", "stiffness in knee", "difficulty walking"],
    "Ankle sprain": ["pain in ankle", "swelling in ankle", "bruising", "difficulty bearing weight"],
    "Sciatica": ["pain radiating from lower back to legs", "numbness in legs", "tingling in legs", "weakness in legs"],
    "Tennis elbow": ["pain in elbow", "weakness in forearm", "difficulty gripping objects", "pain when twisting arm"],
    "Plantar fasciitis": ["pain in heel", "pain in arch of foot", "stiffness in foot", "pain after standing"],
    "Rotator cuff injury": ["pain in shoulder", "weakness in shoulder", "difficulty lifting arm", "pain when lying on affected side"],
    "Hip bursitis": ["pain in hip", "swelling in hip", "pain when lying on affected side", "pain when climbing stairs"]
}

# Expanded conditions_exercises with at least 5-6 exercises per condition
conditions_exercises = {
    "Lower back pain": [
        {"exercise": "Cat-cow stretch", "description": "Start on your hands and knees. Arch your back upwards while exhaling, then lower your back and lift your head while inhaling. Repeat 10 times."},
        {"exercise": "Child's pose", "description": "Kneel on the floor, sit back on your heels, and stretch your arms forward, lowering your chest to the ground. Hold for 30 seconds."},
        {"exercise": "Pelvic tilts", "description": "Lie on your back with knees bent. Tighten your abdominal muscles and push your lower back into the floor. Hold for 5 seconds, repeat 10 times."},
        {"exercise": "Bridges", "description": "Lie on your back with knees bent. Lift your hips off the floor, forming a straight line from knees to shoulders. Hold for 5 seconds, repeat 10 times."},
        {"exercise": "Knee-to-chest stretch", "description": "Lie on your back, pull one knee towards your chest, keeping the other leg straight. Hold for 30 seconds, switch legs."},
        {"exercise": "Bird dog", "description": "Start on hands and knees. Extend one arm forward and the opposite leg back. Hold for 5 seconds, switch sides. Repeat 10 times."}
    ],
    "Neck pain": [
        {"exercise": "Neck tilts", "description": "Sit or stand with your head straight. Slowly tilt your head to one side, bringing your ear towards your shoulder. Hold for 15 seconds, then switch sides."},
        {"exercise": "Chin tucks", "description": "Sit or stand with your head straight. Pull your chin back, creating a 'double chin'. Hold for 5 seconds, repeat 10 times."},
        {"exercise": "Neck rotations", "description": "Sit or stand with your head straight. Slowly turn your head to one side until you feel a stretch. Hold for 15 seconds, then switch sides."},
        {"exercise": "Scalene stretch", "description": "Sit or stand, tilt your head to one side, then rotate it slightly towards the same side. Hold for 15 seconds, switch sides."},
        {"exercise": "Levator scapulae stretch", "description": "Sit or stand, tilt your head to one side, then turn your nose towards your armpit. Hold for 15 seconds, switch sides."},
        {"exercise": "Upper trapezius stretch", "description": "Sit or stand, gently pull your head to one side with your hand. Hold for 15 seconds, switch sides."}
    ],
    "Shoulder impingement": [
        {"exercise": "Pendulum exercise", "description": "Lean forward with one arm hanging down. Gently swing the arm in small circles. Perform for 1 minute, then switch arms."},
        {"exercise": "Wall slides", "description": "Stand with your back against a wall, arms at 90 degrees. Slowly slide your arms up the wall, keeping elbows and wrists in contact. Repeat 10 times."},
        {"exercise": "External rotation with band", "description": "Hold a resistance band with elbows at 90 degrees. Rotate your forearms outward, keeping elbows tucked. Repeat 10 times."},
        {"exercise": "Internal rotation with band", "description": "Hold a resistance band with elbows at 90 degrees. Rotate your forearms inward, keeping elbows tucked. Repeat 10 times."},
        {"exercise": "Scaption raises", "description": "Stand with arms at your sides. Raise your arms to shoulder height at a 45-degree angle, thumbs up. Repeat 10 times."},
        {"exercise": "Doorway stretch", "description": "Stand in a doorway, place your hands on the frame at shoulder height. Step forward to stretch your chest and shoulders. Hold for 30 seconds."}
    ],
    "Knee osteoarthritis": [
        {"exercise": "Quad sets", "description": "Sit with your leg straight. Tighten the muscles on the front of your thigh, pushing the back of your knee into the floor. Hold for 5 seconds, repeat 10 times."},
        {"exercise": "Hamstring stretch", "description": "Sit on the edge of a chair, extend one leg straight, and reach towards your toes. Hold for 30 seconds, switch legs."},
        {"exercise": "Straight leg raises", "description": "Lie on your back with one leg bent. Lift the other leg straight to the height of the bent knee. Repeat 10 times per leg."},
        {"exercise": "Step-ups", "description": "Stand in front of a step. Step up with one foot, then the other, then step down. Repeat 10 times per leg."},
        {"exercise": "Wall squats", "description": "Lean against a wall, slide down into a squat position with knees at 90 degrees. Hold for 10 seconds, repeat 5 times."},
        {"exercise": "Calf raises", "description": "Stand with feet shoulder-width apart. Lift your heels off the ground, then lower. Repeat 15 times."}
    ],
    "Ankle sprain": [
        {"exercise": "Ankle circles", "description": "Sit or lie down, lift one foot, and rotate your ankle in circles. Perform 10 circles in each direction, then switch ankles."},
        {"exercise": "Calf stretch", "description": "Stand facing a wall, place one foot behind you with the heel on the ground. Lean forward to stretch the calf. Hold for 30 seconds, switch legs."},
        {"exercise": "Heel raises", "description": "Stand with feet shoulder-width apart. Lift your heels off the ground, then lower. Repeat 15 times."},
        {"exercise": "Toe raises", "description": "Stand with feet shoulder-width apart. Lift your toes off the ground, then lower. Repeat 15 times."},
        {"exercise": "Balance exercises", "description": "Stand on one leg for 30 seconds, then switch legs. Use a wall for support if needed."},
        {"exercise": "Resistance band exercises", "description": "Sit with legs extended, loop a resistance band around your foot. Push against the band with your foot, repeat 10 times per foot."}
    ],
    "Sciatica": [
        {"exercise": "Piriformis stretch", "description": "Lie on your back with both knees bent. Cross one leg over the other, placing the ankle on the opposite knee. Pull the bottom thigh towards your chest. Hold for 30 seconds, then switch sides."},
        {"exercise": "Knee to chest stretch", "description": "Lie on your back with knees bent. Pull one knee towards your chest, keeping the other foot flat on the floor. Hold for 30 seconds, then switch legs."},
        {"exercise": "Sciatic nerve glide", "description": "Sit on a chair, extend one leg straight, and flex your foot. Slowly lower your head towards your knee. Repeat 10 times per leg."},
        {"exercise": "Seated forward bend", "description": "Sit with legs extended, reach forward towards your toes. Hold for 30 seconds."},
        {"exercise": "Figure-four stretch", "description": "Lie on your back, cross one ankle over the opposite knee. Pull the bottom thigh towards your chest. Hold for 30 seconds, switch sides."},
        {"exercise": "Lumbar extension", "description": "Lie face down, place hands under shoulders, and gently push up, extending your back. Hold for 5 seconds, repeat 10 times."}
    ],
    "Tennis elbow": [
        {"exercise": "Wrist extensor stretch", "description": "Extend one arm in front, palm down. Use the other hand to gently pull the fingers back. Hold for 15 seconds, switch sides."},
        {"exercise": "Forearm pronation and supination", "description": "Hold a light weight, rest your forearm on a table with wrist hanging off. Rotate your wrist to turn palm up and down. Repeat 10 times."},
        {"exercise": "Wrist flexor stretch", "description": "Extend one arm in front, palm up. Use the other hand to gently pull the fingers back. Hold for 15 seconds, switch sides."},
        {"exercise": "Finger extensions", "description": "Place a rubber band around your fingers, spread them apart against the resistance. Repeat 10 times."},
        {"exercise": "Eccentric wrist extensions", "description": "Hold a light weight, rest your forearm on a table with wrist hanging off. Lower the weight slowly, then use the other hand to lift it back. Repeat 10 times."},
        {"exercise": "Towel twist", "description": "Hold a towel with both hands, twist it as if wringing out water. Repeat 10 times in each direction."}
    ],
    "Plantar fasciitis": [
        {"exercise": "Plantar fascia stretch", "description": "Sit with one leg crossed over the other. Pull your toes back towards your shin. Hold for 30 seconds, then switch feet."},
        {"exercise": "Toe curls", "description": "Place a towel on the floor. Use your toes to scrunch the towel towards you. Repeat for 1 minute per foot."},
        {"exercise": "Calf stretch", "description": "Stand facing a wall, place one foot behind you with heel on the ground. Lean forward to stretch the calf. Hold for 30 seconds, switch legs."},
        {"exercise": "Achilles tendon stretch", "description": "Stand on a step with heels hanging off. Lower heels below the step level. Hold for 15 seconds, repeat 5 times."},
        {"exercise": "Marble pickups", "description": "Place marbles on the floor, use your toes to pick them up and place them in a bowl. Repeat for 1 minute."},
        {"exercise": "Towel stretch", "description": "Sit with legs extended, loop a towel around your foot. Pull the towel towards you, stretching the foot. Hold for 30 seconds, switch feet."}
    ],
    "Rotator cuff injury": [
        {"exercise": "External rotation with band", "description": "Hold a resistance band with elbows at 90 degrees. Rotate your forearms outward, keeping elbows tucked. Repeat 10 times."},
        {"exercise": "Scapular squeeze", "description": "Sit or stand with arms at your sides. Squeeze your shoulder blades together. Hold for 5 seconds, repeat 15 times."},
        {"exercise": "Internal rotation with band", "description": "Hold a resistance band with elbows at 90 degrees. Rotate your forearms inward, keeping elbows tucked. Repeat 10 times."},
        {"exercise": "Sleeper stretch", "description": "Lie on your side with affected arm at 90 degrees. Use the other hand to gently push the forearm down. Hold for 15 seconds."},
        {"exercise": "Cross-body stretch", "description": "Bring one arm across your body, use the other hand to pull it closer. Hold for 15 seconds, switch sides."},
        {"exercise": "Pendulum exercise", "description": "Lean forward with one arm hanging down. Gently swing the arm in small circles. Perform for 1 minute, then switch arms."}
    ],
    "Hip bursitis": [
        {"exercise": "Clamshell exercise", "description": "Lie on your side with knees bent. Keeping feet together, lift the top knee. Repeat 15 times per side."},
        {"exercise": "Hip abduction", "description": "Stand with feet shoulder-width apart. Lift one leg to the side, then lower. Repeat 10 times per leg."},
        {"exercise": "Hip bridges", "description": "Lie on your back with knees bent. Lift your hips off the floor, forming a straight line from knees to shoulders. Hold for 5 seconds, repeat 10 times."},
        {"exercise": "Side-lying leg lifts", "description": "Lie on your side, lift the top leg straight up, then lower. Repeat 15 times per side."},
        {"exercise": "Standing hip flexion", "description": "Stand with feet shoulder-width apart. Lift one knee towards your chest, then lower. Repeat 10 times per leg."},
        {"exercise": "Iliotibial band stretch", "description": "Stand with one leg crossed over the other. Lean to the side away from the crossed leg. Hold for 30 seconds, switch sides."}
    ]
}

# Generate Symptoms_to_Condition dataset (100 records per condition)
symptoms_to_condition_data = []
for condition, symptoms in conditions_symptoms.items():
    for _ in range(100):
        num_symptoms = random.randint(1, min(5, len(symptoms)))
        selected_symptoms = random.sample(symptoms, num_symptoms)
        symptoms_text = "I have " + " and ".join(selected_symptoms) + "."
        symptoms_to_condition_data.append({"symptoms": symptoms_text, "condition": condition})

symptoms_to_condition_df = pd.DataFrame(symptoms_to_condition_data)

# Generate Condition_to_Exercises dataset
condition_to_exercises_data = []
for condition, exercises in conditions_exercises.items():
    for exercise_info in exercises:
        condition_to_exercises_data.append({
            "condition": condition,
            "exercise": exercise_info["exercise"],
            "description": exercise_info["description"]
        })

condition_to_exercises_df = pd.DataFrame(condition_to_exercises_data)

# Save to CSV files
symptoms_to_condition_df.to_csv("Symptoms_to_Condition.csv", index=False)
condition_to_exercises_df.to_csv("Condition_to_Exercises.csv", index=False)

print("Datasets generated successfully!")
print(f"Symptoms_to_Condition.csv has {len(symptoms_to_condition_df)} records.")
print(f"Condition_to_Exercises.csv has {len(condition_to_exercises_df)} records.")