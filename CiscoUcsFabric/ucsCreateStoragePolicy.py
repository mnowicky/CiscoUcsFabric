def create_storage_policy(session, base_url, policy_name):
    url = f"{base_url}/storage-policy"
    payload = {
        "name": policy_name,
        "description": "SAN Storage Policy created via Python",
        "storageType": "fc",  # Use 'iscsi' for iSCSI
        "bootPolicy": "boot-from-san",
        "storageAccess": "read-write",
        "associatedStorage": [
            {
                "wwn": "50:00:00:00:00:00:00:01",
                "storageType": "fc",
                "protocol": "fcp",
                "port": "1"
            }
        ]
    }

    response = session.post(url, json=payload)
    if response.status_code == 201:
        print(f"Storage Policy '{policy_name}' created successfully.")
    else:
        print("Failed to create Storage Policy:", response.content)

create_storage_policy(session, base_url, "SAN-Policy-Example")

