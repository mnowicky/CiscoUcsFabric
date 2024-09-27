def delete_service_profile(session, base_url, profile_dn):
    url = f"{base_url}/service-profile/{profile_dn}"

    response = session.delete(url)
    if response.status_code == 204:
        print(f"Service Profile '{profile_dn}' deleted successfully.")
    else:
        print("Failed to delete Service Profile:", response.content)

delete_service_profile(session, base_url, "org-root/ls-SP-Example")

