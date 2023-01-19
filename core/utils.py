classifications = {
    "administrator": "others",
    "Administrative": "others",
    "Assistant": "others",
    'Technician': "others",
    "Specialist": "others",
    "Senior Specialist": "others",
    "Specialist Consultant": "others",
    "Pharmacist": "others",
    "Senior Pharmacist": "others",
    "Consultant Pharmacist": "others",

    'Health Aide': "nursing",
    'Nursing Technician': "nursing",
    "Specialist Nurse": "nursing",
    'Senior Specialist Nurse': "nursing",
    'Consultant Specialist Nurse': "nursing",

}


def get_matching_classification(job_title):
    return classifications.get(job_title, 'doctor')


approvals = dict(
    others=[
        "Financial Affairs Department",
        "Legal Affairs And Compliance",
        "Inventory Control",
        "Health Security",
        "Employee Clinic",
        "Housing Management",
        "E Health",
        "Patient Affairs",
        "Monitoring The Regularity Of Human Resources",
        "Hospital Director",
    ],
    nursing=[
        "Nursing Director",
        "Financial Affairs Department",
        "Legal Affairs And Compliance",
        "Inventory Control",
        "Health Security",
        "Employee Clinic",
        "Housing Management",
        "Pharmacy Dept",
        "Patient Affairs",
        "E Health",
        "Monitoring The Regularity Of Human Resources",
        "Hospital Director",
    ],
    doctor=[
        "Assistant Medical Services",
        "Financial Affairs Department",
        "Legal Affairs And Compliance",
        "Inventory Control",
        "Health Security",
        "Employee Clinic",
        "Housing Management",
        "Patient Affairs",
        "Pharmacy Dept",
        "E Health",
        "Monitoring The Regularity Of Human Resources",
        "Hospital Director",
    ]
)
