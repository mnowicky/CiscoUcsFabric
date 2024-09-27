def create_service_profile(session, base_url, profile_name):
    url = f"{base_url}/service-profile"
    payload = {
        "name": profile_name,
        "orgDn": "org-root",
        "type": "profile",
        "description": "Service Profile created via Python",
        "uuid": "123e4567-e89b-12d3-a456-426614174000"
    }

    response = session.post(url, json=payload)
    if response.status_code == 201:
        print(f"Service Profile '{profile_name}' created successfully.")
    else:
        print("Failed to create Service Profile:", response.content)

create_service_profile(session, base_url, "SP-Example")

