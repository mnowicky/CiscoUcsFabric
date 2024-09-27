def update_lun(session, base_url, lun_name):
    url = f"{base_url}/storage/lun/{lun_name}"
    payload = {
        "description": "Updated LUN Description",
        "size": "200G"  # Example update
    }

    response = session.put(url, json=payload)
    if response.status_code == 200:
        print(f"LUN '{lun_name}' updated successfully.")
    else:
        print("Failed to update LUN:", response.content)

update_lun(session, base_url, "LUN-Example")

