from db import get_db

db=get_db()
collec=db["student_leave"]

def apply_leave(regno,name,leave_date,reason):
    leave_request={
        "regno":regno,
        "name":name,
        "leave_date":leave_date,
        "reason":reason,
        "status":"Pending"
    }
    collec.insert_one(leave_request)
    return "Leave request submitted"
def leave_status(regno):
    result=collec.find({"regno":regno})
    return list(result)

