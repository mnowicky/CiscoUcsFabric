def update_service_profile(session, base_url, profile_dn):
    url = f"{base_url}/service-profile/{profile_dn}"
    payload = {
        "description": "Updated Service Profile Description"
    }

    response = session.put(url, json=payload)
    if response.status_code == 200:
        print(f"Service Profile '{profile_dn}' updated successfully.")
    else:
        print("Failed to update Service Profile:", response.content)

update_service_profile(session, base_url, "org-root/ls-SP-Example")

