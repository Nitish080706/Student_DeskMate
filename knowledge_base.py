from db import get_db

db = get_db()
collec = db["rule_base"]

rules = [
    {
        "intent": "timetable",
        "faq_type": "academic",
        "keywords": ["timetable", "class schedule", "what today"],
        "responses": ["Today classes are Programming in Java 8–10am, DBMS 10am–12pm"]
    },
    {
        "intent": "leave",
        "faq_type": "administration",
        "keywords": ["need leave", "not feeling well", "leave due to sickness", "apply leave"],
        "responses": ["To apply for leave, enter your request for absence"]
    },
    {
        "intent": "exam result",
        "faq_type": "academic",
        "keywords": ["exam", "result", "result date"],
        "responses": ["Exam result will be published on July 4th (Good Luck)"]
    },
    {
        "intent": "placements",
        "faq_type": "career",
        "keywords": ["placements", "company", "company visits", "tcs", "infosys", "zoho"],
        "responses": ["Upcoming placements: TCS on July 28, Infosys on Aug 2, Zoho on July 27"]
    },
    {
        "intent": "courses",
        "faq_type": "academic",
        "keywords": ["credit courses", "additional courses", "courses"],
        "responses": ["Additional courses available: Linux, Sensors and Development"]
    },
    {
        "intent": "library",
        "faq_type": "facilities",
        "keywords": ["library timing", "library hours", "library open"],
        "responses": ["Library is open from 8 AM to 6 PM on weekdays"]
    },
    {
        "intent": "internals",
        "faq_type": "academic",
        "keywords": ["internal marks", "sessional", "test marks"],
        "responses": ["Internal marks will be released by your class advisor next week"]
    },
    {
        "intent": "hostel",
        "faq_type": "facilities",
        "keywords": ["hostel timing", "hostel rules", "hostel in/out"],
        "responses": ["Hostel in-time is 8 PM. Late entry requires prior permission"]
    },
    {
        "intent": "faculty",
        "faq_type": "administration",
        "keywords": ["faculty", "staff", "hod", "professor", "teacher"],
        "responses": ["You can meet your faculty during 12–1 PM or after 4 PM"]
    },
    {
        "intent": "fees",
        "faq_type": "financial",
        "keywords": ["fee", "tuition", "payment", "college fees"],
        "responses": ["College fee last date is August 5. Pay via student portal"]
    }
]

# Safe insertion only if not already present
if collec.count_documents({}) == 0:
    collec.insert_many(rules)
    print("✅ Inserted rules successfully.")
else:
    print("ℹ️ Rules already exist in the database.")
