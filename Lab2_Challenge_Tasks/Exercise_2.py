import random

SURNAME = "Manrique"
SEED_NUM = 7
SIGNAL_LENGTH = 30


def generate_signal(surname, seed_num, length):
    """Generate a unique text-based signal using surname and seed number."""
    generator = random.Random(f"{surname}-{seed_num}")
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()-_=+[]{};:,./?"
    return "".join(generator.choice(characters) for _ in range(length))


def normalize_signal(signal):
    """Remove extra spaces and normalize the signal for processing."""
    normalized = signal.strip()
    normalized = " ".join(normalized.split())
    return normalized


def analyze_signal(signal):
    """Analyze the signal character by character and return statistics."""
    letter_count = 0
    digit_count = 0
    space_count = 0
    special_count = 0
    uppercase_count = 0
    lowercase_count = 0
    char_details = []

    for index, ch in enumerate(signal):
        if ch.isalpha():
            letter_count += 1
            if ch.isupper():
                uppercase_count += 1
            else:
                lowercase_count += 1
        elif ch.isdigit():
            digit_count += 1
        elif ch == " ":
            space_count += 1
        else:
            special_count += 1

        char_details.append(f"[{index}] {ch!r} -> {'Letter' if ch.isalpha() else 'Digit' if ch.isdigit() else 'Space' if ch == ' ' else 'Special'}")

    return {
        "letter_count": letter_count,
        "digit_count": digit_count,
        "space_count": space_count,
        "special_count": special_count,
        "uppercase_count": uppercase_count,
        "lowercase_count": lowercase_count,
        "char_details": char_details,
    }


def classify_signal(stats):
    """Classify the signal based on its content."""
    if stats["special_count"] > 0 and stats["letter_count"] == 0 and stats["digit_count"] == 0:
        return "Special-only signal"
    if stats["letter_count"] > stats["digit_count"] and stats["special_count"] == 0:
        return "Alphabetic signal"
    if stats["digit_count"] > stats["letter_count"] and stats["special_count"] == 0:
        return "Numeric signal"
    if stats["letter_count"] > 0 and stats["digit_count"] > 0 and stats["special_count"] > 0:
        return "Mixed alphanumeric signal with special characters"
    if stats["space_count"] > 0:
        return "Text signal with spacing"
    return "Unclassified signal"


def main():
    generated_signal = generate_signal(SURNAME, SEED_NUM, SIGNAL_LENGTH)
    processed_signal = normalize_signal(generated_signal)
    signal_stats = analyze_signal(processed_signal)
    classification = classify_signal(signal_stats)

    print("=== SIGNAL DIAGNOSTIC REPORT ===")
    print(f"Generated Signal: {generated_signal}")
    print(f"Processed Signal: {processed_signal}")
    print("Character Analysis:")
    for entry in signal_stats["char_details"]:
        print(f"  {entry}")

    print(f"Letter Count: {signal_stats['letter_count']}")
    print(f"Digit Count: {signal_stats['digit_count']}")
    print(f"Space Count: {signal_stats['space_count']}")
    print(f"Special Character Count: {signal_stats['special_count']}")
    print(f"Uppercase Count: {signal_stats['uppercase_count']}")
    print(f"Lowercase Count: {signal_stats['lowercase_count']}")

    print(f"Signal Classification: {classification}")
    print("Execution Log: Signal generated, normalized, and analyzed character by character.")
    print("Final Output: Diagnostic report completed successfully.")


if __name__ == "__main__":
    main()
