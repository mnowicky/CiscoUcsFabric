def create_lun(session, base_url, lun_name, size_gb, storage_policy):
    url = f"{base_url}/storage/lun"
    payload = {
        "name": lun_name,
        "size": f"{size_gb}G",
        "storagePolicy": storage_policy,
        "description": "LUN created via Python",
    }

    response = session.post(url, json=payload)
    if response.status_code == 201:
        print(f"LUN '{lun_name}' created successfully.")
    else:
        print("Failed to create LUN:", response.content)

create_lun(session, base_url, "LUN-Example", 100, "SAN-Policy-Example")

