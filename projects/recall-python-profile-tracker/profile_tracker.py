"""Recall: Python Profile Tracker.

A lightweight console program that stores structured learner profiles and
prints a readable summary for each profile.
"""

learners = [
    {
        "name": "Jade",
        "target_role": "Data Scientist",
        "skill_level": 8,
        "skills": [
            "Data Preprocessing",
            "Exploratory Data Analysis",
            "Data Cleaning",
        ],
        "study_minutes": 60,
        "completed": True,
    },
    {
        "name": "Marco",
        "target_role": "Data Analyst",
        "skill_level": 7,
        "skills": [
            "Trend Analysis",
            "BI Development",
            "Data Storytelling",
        ],
        "study_minutes": 30,
        "completed": True,
    },
    {
        "name": "JM",
        "target_role": "Data Engineer",
        "skill_level": 9,
        "skills": [
            "Data Splitting",
            "Data Training",
            "Data Validation",
        ],
        "study_minutes": 90,
        "completed": False,
    },
]

print("Recall: Python Profile Tracker")
print("=" * 32)

for learner in learners:
    completion_status = "Yes" if learner["completed"] else "No"
    skills_summary = ", ".join(learner["skills"])

    print(f"Learner: {learner['name']}")
    print(f"Target Role: {learner['target_role']}")
    print(f"Current Skill Level: {learner['skill_level']}/10")
    print(f"Skills in Focus: {skills_summary}")
    print(f"Study Minutes Logged: {learner['study_minutes']}")
    print(f"Session Completed: {completion_status}")
    print("-" * 32)
