USERS = {"seoyeon": "sales"}

def check_permission(user, resource, action):
    if user not in USERS:
        return False, "등록되지 않은 사용자"
    return True, "허용"

print(check_permission("seoyeon", "SALES", "QUERY"))
