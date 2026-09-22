"""
Private data and tools for the college lab equipment booking scenario.
"""

# Private college equipment data
EQUIPMENT = {
    "E101": {
        "name": "3D Printer",
        "department": "CSE",
        "status": "Available",
        "available_slots": 2
    },
    "E102": {
        "name": "VR Headset",
        "department": "CSE",
        "status": "Available",
        "available_slots": 4
    },
    "E103": {
        "name": "Arduino Kit",
        "department": "ECE",
        "status": "Issued",
        "available_slots": 0
    },
    "E104": {
        "name": "Raspberry Pi",
        "department": "CSE",
        "status": "Available",
        "available_slots": 3
    }
}


# Private student data
STUDENTS = {
    "S101": {
        "name": "Oviya",
        "department": "CSE",
        "current_booking": "None"
    },
    "S102": {
        "name": "Arun",
        "department": "CSE",
        "current_booking": "E102"
    }
}


def check_equipment(equipment_name):
    """Check equipment availability using the private database."""

    for equipment_id, equipment in EQUIPMENT.items():

        if equipment["name"].lower() == equipment_name.lower():

            return {
                "equipment_id": equipment_id,
                "equipment": equipment["name"],
                "department": equipment["department"],
                "status": equipment["status"],
                "available_slots": equipment["available_slots"]
            }

    return {
        "error": f"Equipment '{equipment_name}' was not found."
    }


def get_booking_details(student_id):
    """Get private booking details for a student."""

    student = STUDENTS.get(student_id)

    if student:
        return {
            "student_id": student_id,
            "name": student["name"],
            "department": student["department"],
            "current_booking": student["current_booking"]
        }

    return {
        "error": f"Student '{student_id}' was not found."
    }


def calculate_late_fine(hours_late):
    """Calculate fine for late equipment return."""

    fine_per_hour = 20
    fine = hours_late * fine_per_hour

    return {
        "hours_late": hours_late,
        "fine_per_hour": fine_per_hour,
        "total_fine": fine
    }
