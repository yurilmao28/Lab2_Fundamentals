SURNAME = "Manrique"
SEED_NUM = 7
ATTEMPT_LIMIT = 3


def generate_password(surname, seed_num):
    """Generate a unique access password using the surname and seed number."""
    return f"{surname.upper()}@{seed_num}"


def authenticate_user(generated_password, attempt_limit, simulated_attempts):
    """Process login attempts and determine the final state of the system."""
    attempts_made = 0
    system_state = "Locked"
    access_result = "Denied"
    execution_log = []

    for attempt in simulated_attempts:
        attempts_made += 1
        if attempt == generated_password:
            access_result = "Granted"
            system_state = "Unlocked"
            execution_log.append(f"Attempt {attempts_made}: Correct password entered.")
            break
        else:
            access_result = "Denied"
            system_state = "Locked"
            execution_log.append(f"Attempt {attempts_made}: Incorrect password entered.")

        if attempts_made >= attempt_limit:
            system_state = "Locked - Maximum attempts reached"
            access_result = "Denied"
            execution_log.append(
                f"Attempt {attempts_made}: Authentication terminated because the allowed limit was reached."
            )
            break

    return {
        "generated_password": generated_password,
        "attempt_limit": attempt_limit,
        "attempts_made": attempts_made,
        "access_result": access_result,
        "system_state": system_state,
        "execution_log": execution_log,
    }


def main():
    generated_password = generate_password(SURNAME, SEED_NUM)
    simulated_attempts = [
        "MANRIQUE@8",
        "MANRIQUE@9",
        generated_password,
    ]

    result = authenticate_user(generated_password, ATTEMPT_LIMIT, simulated_attempts)

    print("=== ACCESS CONTROL SYSTEM ===")
    print(f"Generated Password: {result['generated_password']}")
    print(f"Attempt Limit: {result['attempt_limit']}")
    print(f"Attempts Made: {result['attempts_made']}")
    print(f"Access Result: {result['access_result']}")
    print(f"Final System State: {result['system_state']}")
    print("Execution Log:")
    for entry in result["execution_log"]:
        print(f"  - {entry}")
    print("Final Output: Authentication process completed successfully.")


if __name__ == "__main__":
    main()
