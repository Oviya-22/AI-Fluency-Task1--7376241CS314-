from tools import check_equipment, get_booking_details, calculate_late_fine


def workflow(question):
    """
    Rule-based workflow.
    No LLM is used.
    """

    question_lower = question.lower()

    # Rule 1: Equipment availability
    if "available" in question_lower or "equipment" in question_lower:
        
        if "3d printer" in question_lower:
            return check_equipment("3D Printer")

        elif "vr headset" in question_lower:
            return check_equipment("VR Headset")

        elif "arduino" in question_lower:
            return check_equipment("Arduino Kit")

        elif "raspberry pi" in question_lower:
            return check_equipment("Raspberry Pi")

    # Rule 2: Student booking details
    if "booking" in question_lower or "student" in question_lower:

        if "s101" in question_lower:
            return get_booking_details("S101")

        elif "s102" in question_lower:
            return get_booking_details("S102")

    # Rule 3: Late fine
    if "fine" in question_lower or "late" in question_lower:

        if "2 hours" in question_lower:
            return calculate_late_fine(2)

        elif "5 hours" in question_lower:
            return calculate_late_fine(5)

        elif "10 hours" in question_lower:
            return calculate_late_fine(10)

    return {
        "message": "No predefined rule matches this question."
    }


if __name__ == "__main__":

    print("=== SYSTEM 2: RULE-BASED WORKFLOW ===")

    questions = [
        "Is the 3D Printer available?",
        "Show booking details for S101",
        "What is the fine for 2 hours late?"
    ]

    for question in questions:

        print("\nQ:", question)

        result = workflow(question)

        print("A:", result)