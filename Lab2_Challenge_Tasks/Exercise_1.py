import random


SURNAME = "Manrique"
SEED_NUM = 7
READING_COUNT = 10


def generate_sensor_data(surname, seed_num, count):
	"""Generate repeatable sensor readings from the surname and seed."""
	generator = random.Random(f"{surname}-{seed_num}")
	readings = []

	for _ in range(count):
		if generator.random() < 0.2:
			readings.append(generator.choice(["ERROR", "N/A", "INVALID"]))
		else:
			readings.append(round(generator.uniform(-10, 110), 2))

	return readings


def classify_reading(reading):
	"""Validate a reading and classify it using the operating ranges."""
	try:
		value = float(reading)
	except (TypeError, ValueError):
		return None, "INVALID"

	if value < 20:
		return value, "LOW"
	if value <= 80:
		return value, "NORMAL"
	return value, "HIGH"


sensor_data = generate_sensor_data(SURNAME, SEED_NUM, READING_COUNT)
valid_readings = []
invalid_readings = []
classification_results = []

for reading in sensor_data:
	value, classification = classify_reading(reading)

	if classification == "INVALID":
		invalid_readings.append(reading)
	else:
		valid_readings.append(value)

	classification_results.append((reading, classification))

print("=== SENSOR MONITORING SUMMARY ===")
print(f"Surname: {SURNAME}")
print(f"Seed Number: {SEED_NUM}")
print(f"Generated Sensor Data: {sensor_data}")
print(f"Valid Results: {len(valid_readings)}")
print(f"Invalid Results: {len(invalid_readings)}")
print("Classification Results:")

for reading, classification in classification_results:
	print(f"  {reading!r}: {classification}")

if valid_readings:
	average = sum(valid_readings) / len(valid_readings)
	print(f"Average Valid Reading: {average:.2f}")
else:
	print("Average Valid Reading: None")

print("Execution Log: Sensor readings validated and classified.")
print("Final Output: Sensor monitoring completed successfully.")
