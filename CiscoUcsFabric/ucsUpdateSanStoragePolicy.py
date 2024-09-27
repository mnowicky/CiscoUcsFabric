def update_storage_policy(session, base_url, policy_name):
    url = f"{base_url}/storage-policy/{policy_name}"
    payload = {
        "description": "Updated SAN Storage Policy Description",
        "storageAccess": "read-only"  # Example update
    }

    response = session.put(url, json=payload)
    if response.status_code == 200:
        print(f"Storage Policy '{policy_name}' updated successfully.")
    else:
        print("Failed to update Storage Policy:", response.content)

update_storage_policy(session, base_url, "SAN-Policy-Example")

